import os
import tornado.web
from circle import views


class Application(tornado.web.Application):
    def __init__(self):
        handlers = views.handlers

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            debug = True,
        )

        tornado.web.Application.__init__(self, handlers=handlers, **settings)
