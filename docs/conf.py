from recommonmark.parser import CommonMarkParser

source_parsers = {'.md': CommonMarkParser}

source_suffix = ['.md']
master_doc = 'index'

import datetime
import os
import sys



# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("../.."))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.


# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'


copyright = " %s, EssayHave" % datetime.date.today().year






html_show_sphinx = False
html_favicon = "_static/images/favicon.ico"

html_theme_options = {
    "collapse_navigation": True,

    "style_nav_header_background": "#5bbdbf",
    "style_external_links": True,
    'vcs_pageview_mode': 'edit',

}

html_context = {
    'display_github': 'False',
    'github_user': 'ansible-community',
    'github_repo': 'essayhave',
    'github_version': 'master/docs/',
    'current_version': version,
    'latest_version': 'latest',
    # list specifically out of order to make latest work
    'available_versions': ('latest', ),
    'css_files': (),  # overrides to the standard theme
}

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
# html_style = 'solar.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (within the static path) to place at the top of
# the sidebar.
# html_logo =
# html_logo = "_static/images/logo_big.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/images/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'



# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True

autoclass_content = 'both'

# Note:  Our strategy for intersphinx mappings is to have the upstream build location as the
# canonical source and then cached copies of the mapping stored locally in case someone is building
# when disconnected from the internet.  We then have a script to update the cached copies.
#
# Because of that, each entry in this mapping should have this format:
#   name: ('http://UPSTREAM_URL', (None, 'path/to/local/cache.inv'))
#
# The update script depends on this format so deviating from this (for instance, adding a third
# location for the mappning to live) will confuse it.



linkcheck_workers = 25
# linkcheck_anchors = False
