# Open MP Users Conference Edinburgh 

*link to slides*

*course notes on MPI hybrid and optimization available on request from @cemachelen*

[bestpractice guides](http://www.intertwine-project.eu/best-practice-guides)

## OpenMP 4.5 and Hero 

* [hero github](https://github.com/pulp-platform/hero-sdk)
* hero acceleration (fpga accleration) showed good efficiency
* still has issues with gcc

## Accelerating OpenMP in Climate Models

* M.Glover from Met Office
* Will need to use Nemo with GPUs to couple with LFRic - they also want to use UM on GPUs
* Set up 2 idealised configurations um and nemo to do some testing - 1 node only
* Data movement between GPU and CPU is v.slow
* his initial NEMO tests didn’t show an improvement between gpus and just tiles - the data movement time causes a big slow down 
* at super high resolutions tiling gave the biggest benefits but no “free” benefit from just using gpus
* For UM takes a really long time to compile with the accelerator loaded - had to create a wrapper to only have it loaded for subroutines that required it
* he found even minus the time for moving data the compute time was longer for gpu (for this low res case)
* would require lots of rewriting of the code to make least data movement
* still thought it might go somewhere - meteo suites forecasts already run on gpus

## Lessons from coarse grained OpenMP 

* quantum computational chemistry: flux model
* spoke for a while on improving code efficiently before beginning parallelisation and checking what physics would allow parallelisation
* Gave him a speedup of 36!

## OpenMP in quantum simulations
 
* Youssef Moawad from Glasgow - slides are online - but he spoke super fast
* [personal site](https://devdude.me/) has the slides and github for project

## USEFUL OpenMP

* Jim Conwie
* Scaling results - *Do not use number of threads as x-axis* as using 1 thread instead of 2 has 2 times the cache available etc. Gave an example plotting scatter vs compact affinity where the scatter looked better because it was using more cores when plotted vs threads however this was not the case when plotting vs cores
* `KMP_HW_SUBSET` (intel and LLVM OpenMP only) to set level as limit via sockets, cores or threads 
    * e.g `KMP_HW_SUBSET=1T` only use one thread / core *BUT* you must specify from highest level 
    * like `OMP_NUM_THREADS` you can over subscribe by accident - won’t throw and error
    * should work with MPI
    * [`hwloc` to look at machine](open-mpi.org/projects/hwloc)
    * can set to verbose for investigating `KMP_VERBOSE`
    * set block time to zero if you have an unused thread spinning for no reason (caution)
* openMP5.0 unqualified dynamic schedule is nonmontonic where as in openMP4.5 it would have to be qualified - nonmonotonic is better performing by default 
* Synchronisation hints - openmp.llvm.org - 8 different locks - you can just hint by adding `omp_sync_with_hint` and tell if its contended a lot or not etc code is exactly the same just with added hints  

<hr>

## Cray Tools

* Hybrid applications
* examples run on P100s 
* introduction to perftools e.g pertools-lite -loops or -hbm to profile speed and memory reduced to only at least 1% 
    * allows line level profiling and will show load inbalance
    * hints at `reveal` to look at high level loops e.g timestep loop that can not be vectorised
    * slides should be available later 
    * notes the cray compilers bad autoblocking that need turning off with no blocking
    * again notes the data transfer issue with accelerating with gpus and highlights `cray_acc_debug` env var


## Intel 

* v19 updates and small mention of vtune
* very very quick round up — slides might be circulated