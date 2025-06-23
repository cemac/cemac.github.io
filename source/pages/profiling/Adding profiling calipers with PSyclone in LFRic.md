# Adding PSyclone profiling calipers to UKCA in LFRic 

First, navigate to your PSyclone directory. From here, go to `lib/profiling`. 

Call `make` on the PSyclone library you want to build with (e.g. Vernier/NVIDIA NVTX) in the relevant folder. See the information [here](https://psyclone.readthedocs.io/en/latest/user_guide/profiling.html) on how to do this generically, and the `README.md` in each of the relevant subfolders in the PSyclone GitHub repo for advice on speciific tools.
Make sure you edit the `Makefile` and use the same compiler/flags as you do for your LFRic build! I had segfault issues where I had `-Mchkptr` and `-Mchkstk` enabled in one but not the other. You may also need to point `VERNIER_ROOT` for example to your installed Vernier. 

You also need to interface the PSyData libraries into the build system. See [here]( https://psyclone.readthedocs.io/en/stable/psy_data.html#integrating-psydata-libraries-into-the-lfric-build-environment) for details. The tl;dr of this:

- Create a new folder in a branch of LFRic (`infrastructure/source/psydata`)
- Add the relevant f90 files that you built earlier to this folder. Now they are part of the LFRic source code, they will be analysed, built against and linked into the final binary. 
- I had many issues when trying to get this going trying to get `DependencyAnalyser` (the tool used by LFRic to check dependencies all work before building). I fixed this by adding `vernier_mod` and `vernier` to the list of things for `DependencyAnalyser to ignore` - this is because the libraries are pre-built and linked in (using `-lvernier`, `-lvernier_psy`, `-lvernier_f` and `-lvernier_c` in the Vernier case). You can do this with `export IGNORE_DEPENDENCIES +=...` in your environment/job submission script, or you can amend `infrastructure/build/import.mk` in your LFRic branch.
- Add the includes and libraries - again you can use environment variables in your job submission script. e.g. for Vernier `export LDFLAGS+=' -L<psyclone_path>/lib/profiling/vernier -lvernier_psy -lvernier_f -lvernier_c -lvernier'` and `export FFLAGS+=' -I<psyclone_path>/lib/profiling/vernier`

An important note is to *delete your* `working` *directory* if your build fails and you make changes to the Makefiles etc. when you build them. Whether this is always necessary I'm not sure, but oftentimes I'll make a change (e.g. adding a module to be ignored) and it doesn't pick it up until I do this. 

### Adding the calipers
You can use a transformer to instrument specific loops, or you can simple pass the `--profile routines` option to add instrumentation to all subroutines that you parse with PSyclone. 

The neat thing is that you can apply this to any arbitrary Fortran source code, not just LFRic - in fact it is easier in this case as you don't need to mess around with the complex LFRic build system (this was written before `Fab`/`Baf` were put into routine use, so this comment may be out of date!)

