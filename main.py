
from __future__ import print_function

# [START gae_flex_websockets_app]
from flask import Flask, render_template
from flask_sockets import Sockets
import time
from utils import *


app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/location')
def socket_connection(ws):
    counter =1
    while not ws.closed:
        location = ws.receive()
        if location is None:  # message is "None" if the client has closed.
            continue
        # Send the message to all clients connected to this webserver
        # process. (To support multiple processes or instances, an
        # extra-instance storage or messaging system would be required.)
        #clients = ws.handler.server.clients.values()
        #for client in clients:
            #client.ws.send(message)
        warning_label = dummy_location_search_function(location)
        output_message = "Location {}: {}, Label:, {}".format(counter, location, warning_label)
        counter = counter+1
        ws.send(output_message)
        
# [END gae_flex_websockets_app]


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    print("""
This can not be run directly because the Flask development server does not
support web sockets. Instead, use gunicorn:

gunicorn -b 127.0.0.1:8080 -k flask_sockets.worker main:app

""")
