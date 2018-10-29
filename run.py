from db_create import init_db
from app import socketio, create_app

app = create_app()
init_db()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80)