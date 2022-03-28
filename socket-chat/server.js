const express = require('express')

const PORT = 8080, HOST = '127.0.0.1'
const app = express()

app.use(express.static('public'))
app.use(express.json())

app.get('/', (req, res) => {
    res.send("hello")
})

const chat_route = require('./routes/chat.js')
app.use('/chat', chat_route._Router)

app.listen(PORT, HOST)