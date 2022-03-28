const { Router } = require('express')
const _Router = Router()

_Router.get('/', (req, res) => res.redirect('../index.html'))
_Router.post('/', (req, res) => {
    console.log("msg", req.body)

    res.sendStatus(200)
})

module.exports = { _Router }