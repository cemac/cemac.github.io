# CEMAC GitHub Pages repository

This repository is used to store various documentation, user guides and other miscellaneous information that is hosted on our `github.io` website (https://cemac.github.io). 

## Adding docs
The documentation is contained in various subdirectories in `source/pages`. Please add your page to the most relevant folder, or create a new one.

The repository is set up to automatically parse Markdown and reStructured Text files, so please use one of these formats. Any such files placed in these sub-directories will automatically be added to the table of contents.

Please ensure that you use consistent headings, and that the top-level heading (i.e. a single '`#`' in Markdown) is only used for the overall document title. 

## Steps if creating a new subfolder

If creating a new sub-folder (e.g. if your guide you want to publish doesn't conform to any of the existing categories), you will need to:

1. Create the folder within `source/pages`.
2. Create an `index.rst` file within this page. You can copy `index.rst` from another folder and change the heading (everything above the `=====`). 
3. Add `pages/<foldername>/index.rst` to the `:toctree:` in `source/index.rst`.


