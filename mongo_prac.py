import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://anup0605:mongo0605@mypracticeanup.7r4iu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
print(db)
d = {
    "name": "anup",
    "email": "anupkolkata30@gmail.com",
    "surname": "patra"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
