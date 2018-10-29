from app import socketio, db
from models import Click

def countClicks(id):
    clicks = Click.query.all()
    if len(clicks) == 0:
        return 0
    return [id, clicks[id].count]

def processClick(array):
    id = array[0]
    user = array[1]

    clicks = Click.query.all()
    print clicks
    if len(clicks) == 0:
        c1 = Click(id=0, count=0)
        c2 = Click(id=1, count=0)
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()
    else:
        bob = clicks[id]
        bob.count = bob.count + 1
        db.session.commit()
        socketio.emit('event.update', [id, clicks[id].count, user], broadcast=True)

@socketio.on('event.connect')
def joined(message):
    print "User connected"
    socketio.emit('event.update', countClicks(0), broadcast=True)
    socketio.emit('event.update', countClicks(1), broadcast=True)

@socketio.on('disconnect')
def test_disconnect():
    print "[Client] disconnected"

@socketio.on('connect')
def test_connect():
    print "[Client] connected"

@socketio.on('event.click')
def click(array):
    print array
    processClick(array)