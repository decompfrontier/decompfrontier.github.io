# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Decompfrontier'
copyright = '2023-2024 Arves100'
author = 'Arves100'

release = 'gh-pages'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'myst_parser',
    'sphinx_immaterial'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Display todos by setting to True
todo_include_todos = True

# -- Options for HTML output

html_theme = 'sphinx_immaterial'


html_context = {
  'display_github': True,
  'github_user': 'decompfrontier',
  'github_repo': 'decompfrontier.github.io',
  'github_version': 'master',
  'conf_py_path': '/source/',
}

html_theme_options = {

}

# -- Options for EPUB output
epub_show_urls = 'footnote'
