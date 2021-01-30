# -*- coding: utf-8 -*-
"""
Sphinx documentation configuration file.
"""
# pylint: disable=invalid-name

import datetime

# isort: off
from sphinx_gallery.sorting import (  # pylint: disable=no-name-in-module
    ExplicitOrder,
    FileNameSortKey,
)
from pygmt import __commit__, __version__
from pygmt.sphinx_gallery import PyGMTScraper

# isort: on

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "nbsphinx",
    "sphinx_gallery.gen_gallery",
]

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = []

# Make the list of returns arguments and attributes render the same as the
# parameters list
napoleon_use_rtype = False
napoleon_use_ivar = True

# configure links to GMT docs
extlinks = {
    "gmt-docs": ("https://docs.generic-mapping-tools.org/latest/%s", None),
    "gmt-term": ("https://docs.generic-mapping-tools.org/latest/gmt.conf#term-%s", ""),
}

# intersphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://docs.scipy.org/doc/numpy/", None),
    "pandas": ("http://pandas.pydata.org/pandas-docs/stable/", None),
    "xarray": ("http://xarray.pydata.org/en/stable/", None),
}

sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": [
        "../examples/gallery",
        "../examples/tutorials",
        "../examples/projections",
    ],
    # path where to save gallery generated examples
    "gallery_dirs": ["gallery", "tutorials", "projections"],
    "subsection_order": ExplicitOrder(
        [
            "../examples/gallery/line",
            "../examples/gallery/coast",
            "../examples/gallery/plot",
            "../examples/gallery/grid",
            "../examples/projections/azim",
            "../examples/projections/conic",
            "../examples/projections/cyl",
            "../examples/projections/misc",
            "../examples/projections/nongeo",
            "../examples/projections/table",
        ]
    ),
    # Patter to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": "api/generated/backreferences",
    # Modules for which function level galleries are created.  In
    # this case sphinx_gallery and numpy in a tuple of strings.
    "doc_module": "pygmt",
    # Insert links to documentation of objects in the examples
    "reference_url": {"pygmt": None},
    "image_scrapers": (PyGMTScraper(),),
}

# Sphinx project configuration
templates_path = ["_templates"]
exclude_patterns = ["_build", "**.ipynb_checkpoints"]
source_suffix = ".rst"
needs_sphinx = "1.8"
# The encoding of source files.
source_encoding = "utf-8-sig"
master_doc = "index"

# General information about the project
year = datetime.date.today().year
project = "PyGMT"
copyright = f"2017-{year}, The PyGMT Developers."  # pylint: disable=redefined-builtin
if len(__version__.split("+")) > 1 or __version__ == "unknown":
    version = "dev"
else:
    version = __version__
release = __version__

# These enable substitutions using |variable| in the rst files
rst_epilog = """
.. |year| replace:: {year}
""".format(
    year=year
)

html_last_updated_fmt = "%b %d, %Y"
html_title = "PyGMT"
html_short_title = "PyGMT"
html_logo = ""
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_css_files = ["style.css"]
html_extra_path = []
pygments_style = "default"
add_function_parentheses = False
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True

# Theme config
html_theme = "sphinx_rtd_theme"
html_theme_options = {}
repository = "GenericMappingTools/pygmt"
repository_url = "https://github.com/GenericMappingTools/pygmt"
commit_link = f'<a href="{repository_url}/commit/{ __commit__ }">{ __commit__[:8] }</a>'
html_context = {
    "menu_links": [
        (
            '<i class="fa fa-users fa-fw"></i> Contributing',
            f"{repository_url}/blob/master/CONTRIBUTING.md",
        ),
        (
            '<i class="fa fa-gavel fa-fw"></i> Code of Conduct',
            f"{repository_url}/blob/master/CODE_OF_CONDUCT.md",
        ),
        (
            '<i class="fa fa-book fa-fw"></i> License',
            f"{repository_url}/blob/master/LICENSE.txt",
        ),
        (
            '<i class="fa fa-comment fa-fw"></i> Contact',
            "https://forum.generic-mapping-tools.org",
        ),
        (
            '<i class="fa fa-github fa-fw"></i> Source Code',
            repository_url,
        ),
    ],
    # Custom variables to enable "Improve this page"" and "Download notebook"
    # links
    "doc_path": "doc",
    "galleries": sphinx_gallery_conf["gallery_dirs"],
    "gallery_dir": dict(
        zip(sphinx_gallery_conf["gallery_dirs"], sphinx_gallery_conf["examples_dirs"])
    ),
    "github_repo": repository,
    "github_version": "master",
    "commit": commit_link,
}