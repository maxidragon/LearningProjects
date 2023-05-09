const mongoose = require('mongoose')
const config = require('../config.json')
const url = config.mongooseConnection

mongoose.connect(url)

