import sys
import pathlib

import sphinx.ext.apidoc as apidoc
from recommonmark.parser import CommonMarkParser

caldera_root_dir = pathlib.Path('../../..').absolute()
sys.path.insert(0, str(caldera_root_dir))

from plugins.fieldmanual.utils.plugin_docs import import_plugin_docs
from plugins.fieldmanual.utils.ability_csv import generate_ability_csv


def visit_document(*_):
    pass


# Removes irrelevant warning messages during md file parsing.
# REF: https://github.com/readthedocs/recommonmark/issues/177
# Hopefully will be unnecessary in the future (when recommonmark > 0.6.0 exists)
setattr(CommonMarkParser, 'visit_document', visit_document)


# Call sphinx-apidoc to generate stub files from our source code.
# -o generated: output rst stubs to this directory
# --implicit-namespaces: will find modules in packages without explicit __init__.py
# --force: overwrite existing generated stubs
# ../app/: this is the directory where caldera lives
apidocs_argv = ['-o', '_generated', '--implicit-namespaces', '--force', str(caldera_root_dir / 'app')]
apidoc.main(apidocs_argv)

# Import documentation from plugins
sphinx_root_dir = pathlib.Path.cwd()
print(sphinx_root_dir)
import_plugin_docs(caldera_root_dir, sphinx_root_dir)

# Export csv info to csv:
generate_ability_csv(caldera_root_dir, "_generated/abilities.csv")

# -- Project information -----------------------------------------------------

project = 'caldera'
copyright = '2020, The MITRE Corporation'
author = 'The MITRE Corporation'
master_doc = 'index'


# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'recommonmark',
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_static_path = ['_static']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
