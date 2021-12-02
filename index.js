const io = require("socket.io")
const express = require('express')
const morgan = require('morgan')
const cors = require('cors')

const app = express()
app.use('/', express.static('public'));
app.use(morgan('dev'))
app.use(cors())

app.listen(14045, () => {
    console.log('HTTP server running')
})

const sio = io.listen(14046)

var globalFlag = {}

sio.on('connection', (socket) => {
    socket.on('update', (data) => {
        console.log(data)
        globalFlag = data
        sio.emit('broadcast', globalFlag)
    })
    socket.on('frame', (data) => {
        sio.emit('frame', data)
    })
    socket.on('test', (data) => {
        console.log(data)
    })
})