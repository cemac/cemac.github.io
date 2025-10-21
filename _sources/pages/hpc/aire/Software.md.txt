# Aire software

CEMAC maintain a collection of software applications on the Aire system, which can be accessed via the `module` command.

The build scripts and related files for this software can be found on GitHub:

<https://github.com/cemac/arc>

The content is located on Aire within the directory `/users/cemac`.

## Usage

The `cemac.sh` and `cemac.csh` files can be used to set up the environment for
a `bash` or `csh` shell.

AIRE defaults to `bash` shell, and the following could be added to your
`${HOME}/.bashrc` file:

```
if [ -r /users/cemac/cemac.sh ] ; then
  . /users/cemac/cemac.sh
fi
```

The environment files will do the following:

### Variables

The following variables will be set:

  * `CEMAC_DIR` : will be set to the location of the CEMAC directory,
    `/users/cemac`
  * `CEMAC_SOFTWARE` : will be set to the location of the CEMAC software directory,
    `/users/cemac/software`

## Environment Modules

All modules will be unloaded (`module purge`), and the `MODULEPATH` variable will be unset,
so any centrally provided modules will not be visible.

The modulefiles within the `${CEMAC_SOFTWARE}/modulefiles` directory will be added to the
`MODULEPATH`.

Available software can be viewed by running:

```
module avail
```

Note that some applications are not visible until a dependency has been load.

For example, if you first load the Intel compilers:

```
module load intel
```

The `module avail` command should then show additional software which has been compiled with the Intel compilers.

It is possible to load dependent software in a single command, if the dependency is included.
This command will load the Intel compilers, and appropriate versions of OpenMPI and NetCDF:

```
module load intel openmpi netcdf
```
