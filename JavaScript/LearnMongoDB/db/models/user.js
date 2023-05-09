const mongoose = require("mongoose");

const userSchema = new mongoose.Schema( {
    name: {
        type: String,
        required: true,
        validate(value) {
            if (value === 'admin')
                throw new Error("You can't be an admin lol")
        }
        //unique: true
        //lowercase: true //change to lower letters
    },
    age: {
        type: Number,
        default: 18,
        min: 18
    }
})

// userSchema.pre('save', function(next) {
//     //before save to db
//     this.name += ' is the best!'
//     next()
// })
const User = mongoose.model('User', userSchema)
module.exports = User