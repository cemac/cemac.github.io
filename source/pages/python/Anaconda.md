# Anaconda

The Anaconda Distribution provides a popular method of installing
Python, R and associated libraries and packages.

The Anaconda Distribution (<https://www.anaconda.com/>) is available for
Linux, Windows and Apple systems, and will install all files within your
home directory by default, and as such, installation does not require
any elevated / administrative permissions.

## Installation

There are various different Anaconda installers available, with the
default installation containing Python version 2 or version 3 and many
useful packages (<https://www.anaconda.com/distribution/>). However, it
is worth noting that the installation can require several Gigabytes of
disk space.

As an alternative the Miniconda installer
(<https://docs.conda.io/en/latest/miniconda.html>) provides a minimal
base installation which can be used to create environments and install
required packages.

For Linux systems, the Miniconda 64 bit version 3 installer is
recommended, which can be used to create Python version 2 and version 3
as well as R environments:

<https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>

As mentioned, Anaconda installations can get quite large, and will
install in the home directory by default, so it is worth checking your
quota (`quota -s`) or selecting a suitable location (for example, if you
have access to some large volume disk space) before installation.

The Miniconda installer can be downloaded and made executable with the
following commands:

```
$ wget \
  https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod +x Miniconda3-latest-Linux-x86_64.sh
```

The installer can then be run:

```
$ ./Miniconda3-latest-Linux-x86_64.sh
```

The installation process will ask for the terms of the license to be
accepted, and then ask for an installation directory, defaulting to a
directory named `miniconda3` in the home directory. If you wish to
select an alternative location, enter the full path to the required
location. If installing in your home directory, a sensible path to
choose might be `/home/username/conda`, replacing `username` with your
own username.

After the installer has finished extracting the files in to the selected
location, it will ask whether you wish to run `conda init` to initialise
the installation. Selecting yes will update the `~/.bashrc` so that the
Anaconda programs will be available in future sessions.

Once the installation process has been completed, the installer is no
longer required, and can be removed:

```
$ rm Miniconda3-latest-Linux-x86_64.sh
```

## Initial Configuration

Once the installation is complete, if the `~/.bashrc` file was updated
successfully, the Miniconda installation will be active when you either
run `source ~/.bashrc`, or open a new shell. You should see that the
prompt is now prefixed with `(base)`, to indicate that the base
environment in the Miniconda installation is active:

```
(base) [see1-234:earabc:1]$
```

At this point the `python` command will now default the version of
Python installed with Miniconda, and the `conda` command can be used to
install packages in the `base` environment:

```
(base) [see1-234:earabc:3]$ which python
/home/earabc/conda/bin/python
(base) [see1-234:earabc:3]$ python -V
Python 3.7.4
(base) [see1-234:earabc:4]$ conda install numpy
```

However, an alternative method may be more advisable. Anaconda
environments can include a large number of different programs and
libraries which can cause conflicts with system versions of the same
files, so it can be better to create environments for specific purposes,
activating and deactivating the environments as required.

To stop the `base` environment being automatically activated when a
shell is opened, the following command can be run:

```
$ conda config --set auto_activate_base false
```

It may also be worth adding the `conda-forge` channel to configuration.
The `conda-forge` channel is an additional repository from which
packages can be installed, and includes many popular scientific
packages, such as iris. The following commands will add the
`conda-forge` channel:

```
$ conda config --add channels conda-forge
```

These changes update the file `~/.condarc`, and after they have been run,
and a new shell is opened, the `base` channel will no longer be
activated by default, but the `conda` command will be available to allow
creating new environments:

```
$ which python
/usr/bin/python
$ which conda
/home/earabc/conda/condabin/conda
$ cat ~/.condarc
auto_activate_base: false
channels:
  - conda-forge
  - defaults
```

## Creating Environments

The command `conda create` can be used to create environments containing
the required packages. For example, to create an environment containing
Python version 3 and the Spyder graphical development environment:

```
$ conda create -n py3_spyder python=3 spyder
```

Environments are created within the `envs` directory of the installation
folder, and the environments can be activated and deactivated with the
`conda activate` and `conda deactivate` commands:

```
[see1-234:earabc:12]$ ls conda/envs/
py3_spyder
[see1-234:earabc:12]$ conda activate py3_spyder
(py3_spyder) [see1-234:earabc:13]$ which python
/home/earabc/conda/envs/py3_spyder/bin/python
(py3_spyder) [see1-234:earabc:14]$ python -V
Python 3.7.3
(py3_spyder) [see1-234:earabc:15]$ which spyder
/home/earabc/conda/envs/py3_spyder/bin/spyder
(py3_spyder) [see1-234:earabc:16]$ conda deactivate
[see1-234:earabc:18]$
```

To create a Python version 2 environment containing the `numpy` and
`scipy` packages:

```
$ conda create -n py2_scipy python=2 numpy scipy
```

The available environments can be listed with `conda env list`:

```
$ conda env list
# conda environments:
#
base                  *  /home/earabc/conda
py2_scipy                /home/earabc/conda/envs/py2_spyder
py3_spyder               /home/earabc/conda/envs/py3_spyder
```

## Installing Packages

Once an environment has been activated, additional packages can be
installed within that environment with the `conda install` command:

```
(py3_spyder) [see1-234:earabc:24]$ conda install iris
```

The `conda search` command can be used to search for available packages:

```
(py3_spyder) [see1-234:earabc:25]$ conda search 'obsp*'
Loading channels: done
# Name                       Version           Build  Channel             
obspy                          1.0.2          py27_0  conda-forge         
obspy                          1.0.2          py27_1  conda-forge
...
```

To install a specific version of a package, the version can be specified
with `==`:

```
(py3_spyder) [see1-234:earabc:26]$ conda install obspy==1.0.3
```

It is also possible to install packages using the `pip` command, if a
package is available in the PyPi repositories, but not available in the
Anaconda channels (`pip install packagename`).

The packages which are currently installed in an environment, their
version information and installation source can be viewed by running:

```
(py3_spyder) [see1-234:earabc:27]$ conda list
```

## Updating Packages

The `conda update` command can be used to update packages. For example,
to update `spyder`:

```
(py3_spyder) [see1-234:earabc:28]$ conda update spyder
```

To update all packages in an environment:

```
(py3_spyder) [see1-234:earabc:29]$ conda update --all
```

If an environment is not updated for some time, changes to the
environment (such as installing a new package) may cause version
conflicts, so it may be wise to either create a new environment, or
update all packages in the environment when making changes.

## Installing R

As well as Python environments, the `conda create` command can also be
used to create environments for running the `R` program.

To create an environment containing `R` and `rstudio`:

```
$ conda create -n R R rstudio-desktop
```

This will create an environment named `R`, which can be activated with
`conda activate R`, and once the environment is active the `R` and
`rstudio` programs will be available.
