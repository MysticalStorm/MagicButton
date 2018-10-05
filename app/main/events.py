from flask_socketio import emit
from .. import socketio

clicks = 0

@socketio.on('connect')
def joined():
    print "User connected"

@socketio.on('click')
def click():
    global clicks
    clicks = clicks + 1

    return clicks