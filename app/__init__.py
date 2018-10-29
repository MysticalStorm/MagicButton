from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from config import Config
import eventlet

#eventlet.monkey_patch(socket=True)
#socketio = SocketIO(async_mode='eventlet')
socketio = SocketIO()
db = SQLAlchemy()

def create_app(debug=False):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.debug = True

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    db.init_app(app)

    socketio.init_app(app)
    return app