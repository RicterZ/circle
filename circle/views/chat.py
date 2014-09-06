from circle.base import BaseHandler, BaseSocketHandler


class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')


class ChatSocketHandler(BaseSocketHandler):
    def open(self):
        if not self.session.has_key('username'):
            username = self.request.arguments.get('username')
            self.session.id = str(id(self))
            self.session.username = username[0] if username else self.session.id
        self.clients.add(self)
        self.send_to_all({'message': '%s came in' % self.session.username, 'type': 'sys'})

    def on_close(self):
        self.clients.remove(self)
        self.send_to_all({'message': '%s has left' % self.session.username, 'type': 'sys'})

    def on_message(self, message):
        self.send_to_all({'message': message, 'username': self.session.username, 'type': 'user'})
