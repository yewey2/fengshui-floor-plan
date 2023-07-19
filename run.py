from app import create_app, socketio

app = create_app()
socketio.run(app)
# if __name__ == '__main__':
#     # socketio.run(app, allow_unsafe_werkzeug=True)
#     socketio.run(app)