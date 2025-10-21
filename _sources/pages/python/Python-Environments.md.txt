
:exclamation: 

**2019 - conda made big [improvements](https://www.anaconda.com/how-we-made-conda-faster-4-7/) to speed and space please use conda 4.7**

```bash
conda update conda
conda update --all
conda clean -a
```

:exclamation: 

<hr>

# Managing different python environments

* Either download [anaconda3](https://www.anaconda.com/distribution/#linux)/[miniconda3](https://conda.io/en/latest/miniconda.html) (has both python 2 and 3 available) or use system anaconda (requires some extra configuration to allow working with user home dir rather than system.

1. Create a conda environment
   * `conda create --name <environment-name> python=<version:2.7/3.7>`
2. Activate and install packages e.g:
```bash
conda activate <environment-name>
conda install netcdf4
conda install -c conda-forge iris
```
2. To create a requirements.txt file if using github (allows github picks up dependencies):
   * `conda list -e > requirements.txt` # Save all the info about packages to your folder
3. To export to yml file (so that others can use the same environment)
   * ```
     conda env export --no-builds | grep -v "^prefix: " > environment.yml
     ```
   **NB** the grep pipe removes your personal prefix from the file and the no builds option allow for less future failures

   **NB** conda must be the latest version (bug in the previous version missed pip packages)
4. Tidy up to save space
```bash
conda clean -t # Will remove tarballs
conda clean -p # Will remove packages
conda clean -a # Will do a full clean
```
5. if you have multiple environments you may need a reminder of them:
`conda env list`
6. To save space you can remove and recreate the environment at a later date
`conda env remove --name myenv`
8. The environment can then be picked up again or shared via:
   * `conda env create -f environment.yml`

### Additional information

* To update an environment:
`conda env update --prefix ./env --file environment.yml  --prune`

* To give exact specifications
`conda list --explicit > spec-file.txt`

* Saving environment variables
```bash
cd $CONDA_PREFIX
mkdir -p ./etc/conda/activate.d
mkdir -p ./etc/conda/deactivate.d
touch ./etc/conda/activate.d/env_vars.sh
touch ./etc/conda/deactivate.d/env_vars.sh
```
in activate.d/env_vars.sh
```bash
export MY_KEY='secret-key-value'
export MY_FILE=/path/to/my/file/
```
in deactivate.d/env_vars.sh
```bash 
unset MY_KEY
unset MY_FILE
```

* **NB** wildcard versioning: set major and minor and allow wildcard patch number to pick up bug fixes etc
 * can regex replace `([0-9]).([0-9]).([0-9])` with `$1.$2.*`
 * regex remove builds by `=[a-zA-Z0-9_]*$`