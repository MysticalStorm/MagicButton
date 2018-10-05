from flask_socketio import emit, join_room, leave_room
from .. import socketio

@socketio.on('my event')
def joined(json):
    emit('my response', json)
    return 'OK'
