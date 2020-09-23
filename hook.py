import asyncio
import logging
import pathlib

from aiohttp import web

from app.utility.base_world import BaseWorld


name = 'fieldmanual'
description = 'Holds and serves Caldera documentation'
address = '/plugin/%s/gui' % (name,)
access = BaseWorld.Access.APP

plugin_root = pathlib.Path('plugins/%s' % (name,))
sphinx_docs_root = plugin_root / 'sphinx-docs'
html_docs_root = sphinx_docs_root / '_build' / 'html'


async def landing(_):
    return web.FileResponse(str(plugin_root / 'static' / 'opener.html'))


async def build_docs():
    process = await asyncio.create_subprocess_exec(
        'sphinx-build', '%s/' % (sphinx_docs_root,), str(html_docs_root), '-b', 'html', '-c', str(sphinx_docs_root),
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    logging.debug(stdout)
    if process.returncode:
        logging.error('doc generation failed: %s' % (stderr,))


async def enable(services, loop=None):
    loop = loop if loop else asyncio.get_event_loop()
    html_docs_root.mkdir(parents=True, exist_ok=True)
    loop.create_task(build_docs())
    app_svc = services.get('app_svc')
    app_svc.application.router.add_route('GET', address, landing)
    app_svc.application.router.add_static('/docs/', str(html_docs_root.absolute()), append_version=True)
