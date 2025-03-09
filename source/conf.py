# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'cemac.github.io'
copyright = '2025, Centre for Environmental Modelling and Computation'
author = 'Centre for Environmental Modelling and Computation'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
              'myst_parser', 
              'sphinxemoji.sphinxemoji',
              ]

sphinxemoji_style = 'twemoji'

templates_path = ['_templates']
exclude_patterns = []

source_suffix = ['.rst', '.md']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
