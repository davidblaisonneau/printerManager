#!/usr/bin/python3

from datetime import date
import tornado.escape
from tornado.escape import json_encode
import tornado.ioloop
import tornado.web
from relay import Relay

port = 8888
relayList = [
    Relay(14,""),
    Relay( 4,""),
    Relay(15,""),
    Relay(27,""),
    Relay(22,""),
    Relay(25,""),
    Relay(23,"Delta 1"),
    Relay(24,"Lumiere"),
]

class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '0.0.1',
                     'last_build':  date.today().isoformat() }
        self.write(response)
 
class RelayHandler(tornado.web.RequestHandler):
    def get(self, rid, state):
        if rid=='':
            response = json_encode({i: elt.__dict__ for i,elt in enumerate(relayList)})
        elif int(rid) in range(0, len(relayList)):
            response = json_encode(relayList[int(rid)].__dict__)
        else:
            raise tornado.web.HTTPError(404)
        self.write(response)
    def post(self, rid, state):
        if int(rid) in range(0, len(relayList)):
            print("REST - Set state of {} to {}".format(rid,state))
            if state=='on':
                relayList[int(rid)].on()
            elif state=='off':
                relayList[int(rid)].off()
            response = json_encode({ 'state': relayList[int(rid)].state})
        else:
            raise tornado.web.HTTPError(404)
        self.write(response)

application = tornado.web.Application([
    (r"/relay/(\d*)/?(.*)", RelayHandler),
    (r"/version", VersionHandler)
])
 
if __name__ == "__main__":
    application.listen(port)
    print("Server started on port {}".format(port))
    tornado.ioloop.IOLoop.instance().start()
