import asyncio
import logging
import pathlib

import concurrent.futures
from aiohttp import web

from app.utility.base_world import BaseWorld


name = 'fieldmanual'
description = 'Holds and serves Caldera documentation'
address = '/plugin/%s/gui' % (name,)
access = BaseWorld.Access.APP

plugin_root = pathlib.Path('plugins/%s' % (name,))
sphinx_docs_root = plugin_root / 'sphinx-docs'
html_docs_root = sphinx_docs_root / '_build' / 'html'

logger = logging.getLogger('fieldmanual')


async def landing(_):
    return web.FileResponse(str(plugin_root / 'static' / 'opener.html'))


def _run_sphinx_build():
    import sys
    import io

    import sphinx.cmd.build

    out = io.StringIO()
    err = io.StringIO()
    sys.stdout = out
    sys.stderr = err

    argv = ['%s/' % (sphinx_docs_root,), str(html_docs_root), '-b', 'html', '-c', str(sphinx_docs_root)]

    sphinx.cmd.build.main(argv)

    out.seek(0)
    err.seek(0)
    return out.read(), err.read()


async def build_docs(loop=None):
    loop = loop or asyncio.get_event_loop()
    with concurrent.futures.ProcessPoolExecutor() as pool:
        try:
            out, err = await loop.run_in_executor(pool, _run_sphinx_build)
        except Exception:
            logger.warning("Encountered problem while building documentation.", exc_info=True)

        if 'build succeeded' in out and err:
            logger.info('Docs built successfully with the following warnings\n%s' % err)
        elif 'build succeeded' in out:
            logger.info('Docs built successfully.')
        else:
            logger.warning('Unable to build docs:\n%s' % err)


async def enable(services, loop=None):
    loop = loop if loop else asyncio.get_event_loop()
    html_docs_root.mkdir(parents=True, exist_ok=True)
    loop.create_task(build_docs(loop=loop))
    app_svc = services.get('app_svc')
    app_svc.application.router.add_route('GET', address, landing)
    app_svc.application.router.add_static('/docs/', str(html_docs_root.absolute()), append_version=True)
