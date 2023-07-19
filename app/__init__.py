from flask import Flask

from .events import socketio

from .routes import main

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secretkey"

    # socketio = SocketIO(app)
    app.register_blueprint(main)

    socketio.init_app(app)

    return app