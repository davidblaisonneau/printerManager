#!/usr/bin/python

from datetime import date
import tornado.escape
from tornado.escape import json_encode
import tornado.ioloop
import tornado.web
from relay import Relay

port = 8888
relayList = [
    Relay(14,""),
    Relay(04,""),
    Relay(15,""),
    Relay(27,""),
    Relay(22,""),
    Relay(25,""),
    Relay(23,"Delta 1"),
    Relay(24,"Lumière"),

]

class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '0.0.1',
                     'last_build':  date.today().isoformat() }
        self.write(response)
 
class RelayHandler(tornado.web.RequestHandler):
    def get(self, id):
        if !id:
            response = json_encode(relayList)
        self.write(response)

 
application = tornado.web.Application([
    (r"/relay/(.*)", RelayHandler),
    (r"/version", VersionHandler)
])
 
if __name__ == "__main__":
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    print("Server started on port {}".format(port))
