import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure = False)
dns.resolver.default_resolver.nameservers = ["1.1.1.1"]


import pymongo
import pprint

client = pymongo.MongoClient("mongodb+srv://three:iamuser@cluster0.y0bsh.mongodb.net/testdb?retryWrites=true&w=majority")

def insert():
  db = client.testdb

  collection = db.data

  post = {"test":None, "dict" :"new"}

  id = collection.insert_one(post).inserted_id

  print (id)

def pull():
  db = client.testdb

  collection = db.data

  pprint.pprint(collection.find_one({"test":None}))

pull()
