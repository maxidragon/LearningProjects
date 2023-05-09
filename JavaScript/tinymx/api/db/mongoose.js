const mongoose = require('mongoose')
const config = require("../config.json")
const connectionString = process.env.DB || config.connectionString

const URL = require('./models/URL')

//connect to db
mongoose.connect(connectionString, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})

const connection = mongoose.connection

module.exports = connection