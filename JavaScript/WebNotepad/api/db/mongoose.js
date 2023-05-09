const mongoose = require('mongoose')
const config = require("../config.json")
const url = config.connectionString

const Note = require('./models/note')
//connect to db
mongoose.connect(url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})


