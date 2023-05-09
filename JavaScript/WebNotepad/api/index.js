const express = require('express')
const bodyParser = require('body-parser')

const app = express()
const config = require("./config.json")
const port = process.env.PORT || config.port
const apiRouter = require('./routes/api')

//db
require('./db/mongoose')
//parser
//content-type: application/json
app.use(bodyParser.json())

//routes
app.use('/api/', apiRouter)

//app
app.listen(port, function() {
    console.log('Listening on port ' + port + '...')
})