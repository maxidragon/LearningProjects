require('./db/db')

const mongoose = require("mongoose");
const User = require('./db/models/user')



//createUser({name: 'Nicole', age: 17})//I can insert age "17" and mongoose will convert it)
const createUser = async (data) => {
    try {
    const user = new User(data)
    await user.save()
    console.log(user)
    }
    catch (error) {
        console.log(error)
    }
}

const findUsers = async (data) => {
    try {
        const users = await User.find(data)
        console.log(users)
    }
    catch(error) {
        console.log(error)
    }
}
// createUser({
//     name: 'Cale',
//     age: 23
// })
createUser({
    name: 'admin',
    age: 19
})
// findUsers({
//
// })