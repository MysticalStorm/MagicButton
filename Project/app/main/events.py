from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

@socketio.on('my event')
def joined(json):
    print("SOCKET EVENT")
    print('received json: ' + str(json))
