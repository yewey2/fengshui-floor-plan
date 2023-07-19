from flask_socketio import emit
from .extensions import socketio
from flask import request
from app.image_overlay import overlay

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
    # print('data is', data)
    print(data.get('angle'))
    # negative angle to rotate acw
    img = overlay(data.get('img'), angle=-float(data.get('angle')), center=data.get('center'))
    print(img)
    emit('display_img', {'img': img})
