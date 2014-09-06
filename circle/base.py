import json

import tornado.web
import tornado.websocket
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

from circle.utils import Storage


class JinjaTemplateMixin(object):
    """A simple mixin of jinja2

    From: http://bibhas.in/blog/using-jinja2-as-the-template-engine-for-tornado-web-framework/
    """
    def jinja2_render(self, template_name, **kwargs):
        env = Environment(loader=FileSystemLoader(self.settings['template_path']))

        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
        return template.render(settings=self.settings, **kwargs)


class BaseHandler(tornado.web.RequestHandler, JinjaTemplateMixin):
    def render(self, template_name, **kwargs):
        """Override render method
        """
        self.write(self.jinja2_render(template_name, **kwargs))


class BaseSocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    def __init__(self, application, request, **kwargs):
        self.session = Storage()
        tornado.websocket.WebSocketHandler.__init__(self,application, request, **kwargs)

    @staticmethod
    def send_to_all(message):
        for client in BaseSocketHandler.clients:
            client.write_message(json.dumps(message))

