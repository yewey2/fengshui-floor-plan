from flask_socketio import emit
from .extensions import socketio
from flask import request
from app.image_overlay import overlay

from timeit import default_timer as timer

# request.sid => The session id of the user 
# can use it to identify if it is the same user

all_users = dict()

@socketio.on("connect")
def handle_connect():
    print("Connected Python")

@socketio.on("my event")
def handle_my_event(data=dict()):
    print('data is', data)

@socketio.on("process_image")
def handle_my_event(data):
    # negative angle to rotate acw
    print('processing image')
    start = timer()
    img = overlay(data.get('img'), angle=-float(data.get('angle')), center=data.get('center'))
    end = timer()
    print('processed image after', end-start)
    emit('display_img', {'img': img})
