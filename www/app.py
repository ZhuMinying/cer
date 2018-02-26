#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Web Application for Cheese Egg Roll'

__author__ = 'Patrick'


import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time


from datetime import datetime

from aiohttp import web


# define the urls 
def index(request):
    return web.Response(body=b'<h1>Hello, this is my first website!</h1>',content_type='text/html')

def menmen(request):
    return web.Response(body=b'<h1>This website is for XX and MM. Xiangxiang LOVE Menmen!</h1>',content_type='text/html')


# define the app and server with asyncio
def init(loop):
    app = web.Application(loop=loop)
    # combine the urls
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/menmen', menmen)
    # make a server
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000) 
    # do a log
    logging.info('Server started at 127.0.0.1:9000')
    return srv


# make a loop to run the application
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
