# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinxdocs'
copyright = '2023, RMR'
author = 'RMR'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = ['myst_parser']
source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


# THEMES          
# https://www.sphinx-doc.org/en/master/usage/theming.html
# https://sphinx-themes.org/
# built-in         classic traditional agogo nature haiku sphinxdoc 
# mobile-friendly   alabaster scrolls
# press furo 
# sphinx_book_theme piccolo_theme 
# sphinx_material sphinxawesome_theme sphinx_readable_theme

html_theme = 'readable'

html_static_path = ['_static']


# EDIT THE SOURCE
# https://docs.readthedocs.io/en/stable/guides/edit-source-links-sphinx.html

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "rafael5", # Username
    "github_repo": "MyDoc", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/source/", # Path in the checkout to the docs root
}

{% if display_github %}
    <li><a href="https://github.com/{{ github_user }}/{{ github_repo }}
    /blob/{{ github_version }}{{ conf_py_path }}{{ pagename }}.rst">
    Show on GitHub</a></li>
{% endif %}

