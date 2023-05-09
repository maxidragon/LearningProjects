import axios from 'axios'
const config = require('./config.json')

const instance = axios.create({
    baseURL: config.baseURL,
    headers: {
        'Content-Type': 'application/json'
    }
})

export default instance