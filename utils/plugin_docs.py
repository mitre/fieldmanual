
import os
from distutils.dir_util import copy_tree
from jinja2 import Environment, FileSystemLoader


# Directory in plugin to pull documentation from
PLUGIN_DOCS_DIR = 'docs'


def import_plugin_docs(caldera_root_dir, sphinx_root_dir):
    doc_paths = copy_plugin_docs(caldera_root_dir, sphinx_root_dir)
    create_index(sphinx_root_dir, doc_paths)


def copy_plugin_docs(caldera_root_dir, sphinx_root_dir):
    """Copy docs from plugins to sphinx-docs/plugins/{plugin_name}/

    :param caldera_root_dir: Path to CALDERA base directory
    :param sphinx_root_dir: Path to sphinx directory
    :return: List of copied Markdown and reStructuredText files
    """
    sphinx_plugins_dir = os.path.abspath(os.path.join(sphinx_root_dir, 'plugins'))
    caldera_plugins_dir = os.path.abspath(os.path.join(caldera_root_dir, 'plugins'))
    doc_paths = []

    for f in os.scandir(caldera_plugins_dir):
        if not f.is_dir():
            continue

        plugin_docs_dir = os.path.join(f.path, PLUGIN_DOCS_DIR)
        if not os.path.isdir(plugin_docs_dir):
            continue

        sphinx_plugin_dir = os.path.join(sphinx_plugins_dir, f.name)
        if not os.path.exists(sphinx_plugin_dir):
            os.makedirs(sphinx_plugin_dir)

        copied_files = copy_tree(plugin_docs_dir, sphinx_plugin_dir)
        for doc_file in copied_files:
            if doc_file.endswith('.md') or doc_file.endswith('.rst'):
                doc_paths.append(os.path.relpath(doc_file, sphinx_root_dir))

    return doc_paths


def create_index(sphinx_root_dir, plugin_doc_paths):
    """Create index.rst from Jinja2 template

    :param sphinx_root_dir: Path to sphinx directory
    :param plugin_doc_paths: List of copied files to add to index
    """
    env = Environment(loader=FileSystemLoader(searchpath=str(sphinx_root_dir)))
    index_template = env.get_template('index.rst.j2')
    index_content = index_template.render(plugin_docs=plugin_doc_paths)

    with open(os.path.join(sphinx_root_dir, 'index.rst'), 'w') as f:
        f.write(index_content)
