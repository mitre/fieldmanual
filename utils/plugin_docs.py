
import os
from distutils.dir_util import copy_tree
from jinja2 import Environment, FileSystemLoader


DOCS_DIR = 'docs'


def import_plugin_docs(caldera_dir):
    sphinx_dir = os.getcwd()
    doc_paths = copy_plugin_docs(caldera_dir, sphinx_dir)
    create_index(sphinx_dir, doc_paths)


def copy_plugin_docs(caldera_dir, sphinx_dir):
    """Copy docs from plugins to sphinx-docs/plugins/{plugin_name/

    :param caldera_dir: Path to CALDERA base directory
    :param sphinx_dir: Path to sphinx directory
    :return: List of copied Markdown and reStructuredText files
    """
    sphinx_plugins_dir = os.path.abspath(os.path.join(sphinx_dir, 'plugins'))
    plugins_dir = os.path.abspath(os.path.join(caldera_dir, 'plugins'))
    doc_paths = []

    for f in os.scandir(plugins_dir):
        if f.is_dir():
            plugin_dir = f.path
            plugin_docs_dir = os.path.join(plugin_dir, DOCS_DIR)
            if os.path.isdir(plugin_docs_dir):
                plugin_name = f.name
                plugin_sphinx_dir = os.path.join(sphinx_plugins_dir, plugin_name)

                if not os.path.exists(plugin_sphinx_dir):
                    os.makedirs(plugin_sphinx_dir)
                copied_files = copy_tree(plugin_docs_dir, plugin_sphinx_dir)

                for doc_file in copied_files:
                    if doc_file.endswith('.md') or doc_file.endswith('.rst'):
                        doc_paths.append(os.path.relpath(doc_file, sphinx_dir))
    return doc_paths


def create_index(sphinx_dir, doc_paths):
    """Create index.rst from Jinja2 template

    :param sphinx_dir: Path to sphinx directory
    :param doc_paths: List of copied files to add to index
    """
    env = Environment(loader=FileSystemLoader(searchpath=sphinx_dir))
    index_template = env.get_template('index.rst.j2')
    index_content = index_template.render(plugin_docs=doc_paths)

    with open(os.path.join(sphinx_dir, 'index.rst'), 'w') as f:
        f.write(index_content)
