import tornado.ioloop
import tornado.httpserver
from circle import Application


if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8000)

    tornado.ioloop.IOLoop.instance().start()