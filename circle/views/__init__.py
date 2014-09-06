from circle.views.chat import IndexHandler, ChatSocketHandler


handlers = [
    ('/', IndexHandler),
    ('/chat', ChatSocketHandler),
]