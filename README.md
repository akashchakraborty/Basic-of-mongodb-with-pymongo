All MongoDb commands you will ever need (MongoDb Cheatsheet)

In this post, we will see a comprehensive list of all the MongoDB commands you will ever need as a MongoDB beginner. This list covers almost all the most used commands in MongoDB.

I will assume that you are working inside a collection named 'comments' on a MongoDB database of your choice
## Database Commands
View all databases

```shell
show dbs
```

Create a new or switch databases 

```shell
use dbName
```

View current Database

```shell
db
```

Delete Database 

```shell
db.dropDatabase()
```

## Collection Commands

Show Collections

```shell
show collections
```

Create a collection named 'comments'

```shell
db.createCollection('comments')
```

Drop a collection named 'comments'

```shell
db.comments.drop()
```

## Row(Document) Commands

Show all Rows in a Collection 

```shell
db.comments.find()
```

Show all Rows in a Collection (Prettified)

```shell
db.comments.find().pretty()
```

Find the first row matching the object

```shell
db.comments.findOne({name: 'Harry'})
```

Insert One Row

```shell
db.comments.insert({
    'name': 'Harry',
    'lang': 'JavaScript',
    'member_since': 5
 })
```

Insert many Rows

```shell
db.comments.insertMany([{
    'name': 'Harry',
    'lang': 'JavaScript',
    'member_since': 5
    }, 
    {'name': 'Rohan',
    'lang': 'Python',
    'member_since': 3
    },
    {'name': 'Lovish',
    'lang': 'Java',
    'member_since': 4
}])
```

Search in a MongoDb Database

```shell
db.comments.find({lang:'Python'})
```

Limit the number of rows in output

```shell
db.comments.find().limit(2)
```

Count the number of rows in the output

```shell
db.comments.find().count()
```

Update a row

```shell
db.comments.updateOne({name: 'Shubham'},
{$set: {'name': 'Harry',
    'lang': 'JavaScript',
    'member_since': 51
}}, {upsert: true})
```

Mongodb Increment Operator

```shell
db.comments.update({name: 'Rohan'},
{$inc:{
    member_since: 2
}})
```

Mongodb Rename Operator

```shell
db.comments.update({name: 'Rohan'},
{$rename:{
    member_since: 'member'
}})
```

Delete Row 

```shell
db.comments.remove({name: 'Harry'})
```

Less than/Greater than/ Less than or Eq/Greater than or Eq

```shell
db.comments.find({member_since: {$lt: 90}})

db.comments.find({member_since: {$lte: 90}})

db.comments.find({member_since: {$gt: 90}})

db.comments.find({member_since: {$gte: 90}})
```