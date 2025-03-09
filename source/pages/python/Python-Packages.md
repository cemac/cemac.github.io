# Information on Packaging up Python #

*in progress*

# Docstring example # 

Here's example python doc string, containing information on the project
i.e. a link to the funder, the fact it was done by CEMAC and therefore 
credit the university. Remember to include the scientists names that this 
is for or who started the work or initiated the science behind the code. 

Here the doc-string follows a [PEP 257](https://www.python.org/dev/peps/pep-0257/) 
convention. Essentially use this formatting and users of the code will be able
to perform ```help(mypythonmodule)``` to access the top level doc string 
and ```help(mypythonmodule.func1)``` to access the relevant info on functions 
with in your module. 

```python
"""mypythonmodule a box

This module was developed by CEMAC (Leeds University) as part of the XXXX Project.
This scripts build on Work done by XXXX, doing this task and using
this information. 

Example:
    To use::
        import mypythonmodule
        c = mypythonmodule(arg1, arg2, arg3, karg=Val)

Attributes:
    dataroot(str): A string containing path to data 
    constant(float): A variable defined e.g. gravity 9.81 m/s**2

.. CEMAC_mypythonmodule:
   https://github.com/cemac/mypythonmodules_repo
"""
```

<hr>

## Packaging #

### BASIC ##

At the very least setting up a requirements.txt should done

**Method 1 - Conda**

1. Create a conda environment
   * `conda create --name <environment-name> python=<version:2.7/3.5>`
2. To create a requirements.txt file:
   * `conda list -e > requirements.txt` #Save all the info about packages to your folder
3. To export to yml file
   * ```
     conda activate <environment-name>
     conda env export | grep -v "^prefix: " > environment.yml
     ```
   **NB** the grep pipe removes your personal prefix from the file
4. The environment can then be used:
   * `conda env create -f environment.yml`


**Method 2 - Pipenv**

James's prefered method, use pipenv which creates a pip.lock file. NB, some packages such as iris are not pip installable, most notably iris and conda install tend to be slightly faster.