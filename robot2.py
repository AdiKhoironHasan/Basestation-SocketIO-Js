import socketio
from time import sleep

sio = socketio.Client()
sio.connect('http://localhost:14046')

c = 0
while 1 :
    c = c+1
    data = [
        {
            'id_robot' : 1,
            'id_item' : 0,
            'name' : 'bola',
            'value' : [c, c+1],
        },
        {
            'id_robot' : 1,
            'id_item' : 1,
            'name' : 'gawang',
            'value' : [c, c+1],
        },
        {
            'id_robot' : 1,
            'id_item' : 2,
            'name' : 'dummy',
            'value' : [c, c+1],
        },
        {
            'id_robot' : 1,
            'id_item' : 3,
            'name' : 'company',
            'value' : [c, c+1],
        },
    ]
    print(data)
    sio.emit('update', data)
    sleep(0.6)