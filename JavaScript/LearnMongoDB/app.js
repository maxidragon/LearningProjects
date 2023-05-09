const { MongoClient, ServerApiVersion, ObjectID} = require('mongodb')
const config = require('./config.json')
const uri = config.connectionString

const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 });

client.connect(function(err, db) {
    if (err) throw err;
    var test = db.db("test");
    var restaurants = db.db("sample_restaurants");
    // var query = {borough : "Brooklyn"};
    // restaurants.collection("restaurants").find(query).toArray(function(err, result) {
    //     if (err) throw err;
    //     console.log(result);
    //     db.close();
    // });
    // test.collection('users').insertOne({
    //     name: 'Tom',
    //     age: 25
    // }, (error, result) => {
    //     if (error)
    //         console.log('error', error)
    //     console.log(result)
    //     db.close()
    // })
    //.insertMany array to insert many documents

    // test.collection("users").find().count(function(err, result) {
    //     if (err) throw err
    //     console.log(result)
    //     db.close()
    // });
    // test.collection('users').updateOne({
    //     age: 25
    // }, {
    //     $set: {
    //         age: 35
    //     }
    // })
    // test.collection("users").find({
    //     age: {$gt: 24}//gt - greater than
    // }).toArray(function(err, result) {
    //     if (err) throw err
    //     console.log(result)
    //     db.close()
    // });

    // test.collection('users').updateMany({
    //     age: 24
    // }, {
    //     $set: {
    //         age: 25
    //     }
    // })
    // test.collection("users").deleteMany({
    //     age: 25
    // }, (error, result) => {
    //         if (error)
    //             console.log('error', error)
    //         console.log(result)
    //         db.close()
    //     })
    // const id = new ObjectID("639622f9a5b29b91347caed2")
    // console.log(id.getTimestamp())
    //const id = new ObjectID() //i can use it in creating user, _id: id
    test.collection("users").findOne(
        {
            _id: new ObjectID("639622f9a5b29b91347caed2")
        }, (err, result) => {
        if (err) throw err
        console.log(result)
        db.close()
    });
    // test.collection("users").find().toArray(function(err, result) {
    //     if (err) throw err
    //     console.log(result)
    //     db.close()
    // });
});
