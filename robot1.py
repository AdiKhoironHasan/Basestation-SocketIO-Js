import socketio
from time import sleep

sio = socketio.Client()
sio.connect('http://localhost:14046')

@sio.event
def broadcast(data):
    print(data)

c = 0
while 1 :
    c = c+1
    data = [
        {
            'id_robot' : 0,
            'id_item' : 0,
            'name' : 'bola',
            'value' : [c, c+1],
        },
        {
            'id_robot' : 0,
            'id_item' : 1,
            'name' : 'gawang',
            'value' : [c, c+1],
        },
        {
            'id_robot' : 0,
            'id_item' : 2,
            'name' : 'dummy',
            'value' : [c, c+1],
        },
        {
            'id_robot' : 0,
            'id_item' : 3,
            'name' : 'company',
            'value' : [c, c+1],
        },
        {
            'id_robot' : 0,
            'id_item' : 5,
            'name' : 'getBall',
            'value' : 1,
        }
    ]
    # print(data)
    sio.emit('update', data)
    sleep(1)