import pymongo


########################################### FUNCTIONS #############################################

#connecting to the mongo client
def connect_client():
    client = pymongo.MongoClient("mongodb://localhost:27017/") # creating a connection
    return client

# inserting one document
def insert_one_doc(dict1: dict, collection):
    collection1 = collection.insert_one(dictionary) #inserting the created document into the collection
    return collection1

# inserting multiple documents
def insert_many_doc(list1: list,collection): # we can also insert multiple items at once
    collection.insert_many(list1) # inserting multiple documents/dictionaries

# finding a single document
def find_one_doc(collection,param=None):
    one = collection.find_one(param)
    return one

# def find_many_doc(collection,*params):
#     many=collection.find({"$and": list(params)})
#     for i in many:
#         print(i)

def find_many_doc(collection, filter=None, projection=None):
    many = collection.find(filter=filter, projection=projection)
    for doc in many:
        print(doc)

def update_one_doc(collection,prevval,nextval):
    return collection.update_one(prevval, {'$set': nextval})

def update_many_doc(collection,prevval,nextval):
    return collection.update_many(prevval, {'$set': nextval})

def delete_one_doc(collection,*params):
    return collection.delete_one(*params)

def delete_many_doc(collection,*params):
    return collection.delete_many(*params)

########################################## DOCUMENTS ##############################################

# creating a document to be inserted into that collection
dictionary = {'name':'akash','marks':98} 

# creating list of dictionaries for multiple entries
students = [
        {"name": "Alice", "location":"Kualalampur","marks": 80},
        {"name": "Bob","location":"Dubai", "marks": 75},
        {"name": "Charlie","location":"Guwahati", "marks": 90},
        {"name": "David", "location":"Hyderabad","marks": 65},
        {"name": "Malice","location":"Delhi","marks": 80},
        {"name": "Knob","location":"Kolkata", "marks": 75},
        {"name": "Harlie","location":"Bangalore", "marks": 90},
        {"name": "Davidson","location":"Mumbai", "marks": 65},
        {"name": "Alice", "location":"Kualalampur","marks": 80},
        {"name": "Bob","location":"Dubai", "marks": 75},
        {"name": "Charlie","location":"Guwahati", "marks": 90},
        {"name": "David", "location":"Hyderabad","marks": 65}
    ]

# we can also manually create the id field and their values
students2 = [
        {"_id":1,"name": "Malice","location":"Delhi","marks": 80},
        {"_id":2,"name": "Knob","location":"Kolkata", "marks": 75},
        {"_id":3,"name": "Harlie","location":"Bangalore", "marks": 90},
        {"_id":4,"name": "Davidson","location":"Mumbai", "marks": 65},
        {"_id":5,"name": "Alice", "location":"Kualalampur","marks": 80},
        {"_id":6,"name": "Bob","location":"Dubai", "marks": 75},
        {"_id":7,"name": "Charlie","location":"Guwahati", "marks": 90},
        {"_id":8,"name": "David", "location":"Hyderabad","marks": 65}
    ]

########################################## DRIVER CODE ############################################

if __name__ == "__main__":
    
    db_name = "Akash3"
    collection_name = "mySampleCollectionForAkash"

    client=connect_client()
    res1=str(client)
    if "connect=True)" in res1:
        print("Connection Successful")
    else:
        print("Client Connection Unsuccessful")

    print(client.list_database_names()) # gets all the db names

    db = client[db_name] # creating a db or use that db
    res1=str(db)
    if "connect=True)" and db_name in res1:
        print("Database Connection/Creation Successful")
    else:
        print("Database Connection Unsuccessful")
    
    print(db.list_collection_names()) # printing collection names   

    collection=db[collection_name] # creating a collection or using it
    res1 = str(collection)
    if "connect=True)" and db_name and collection_name in res1:
        print("Collection Connection/Creation Successful")
    else:
        print("Collection Connection/Creation Unsuccessful")


    insert_one_doc(dictionary,collection)
    insert_many_doc(students2,collection)
    onedoc = find_one_doc(collection,{'name':'akash'}) # Even if a particular name has 2 entries then also it will give 1 as it finds only 1
    print(onedoc)
    manydoc = find_many_doc(collection,{'name':'Malice','marks':80}) # find the doc in the collection of the db where name is malice and marks is 80
    manydoc2 = find_many_doc(collection,{'name':'akash'},{'name':1,'_id':0}) # finds the docs where name is malice and returns only the name and not anything else
    update_one_doc(collection,{'name':'Alice'},{'marks':2}) # updates the marks to 20 where name is Alice
    update_one_doc(collection,{'name':'Alice','location':'Surat'},{'marks':100}) # updates the marks to 20 where name is Alice and loc is surat
    up = update_many_doc(collection,{'name':'Alice'},{'location':'Mathura'}) # updates all location where name is alice
    print(up.modified_count) # gives the count as to how many docs have been modified
    delete_one_doc(collection,{'name':'Jhatu','location':'chutiyapur'}) # deletes the document with the particular name and location
    dl = delete_many_doc(collection,{'name':'Jhatu'}) # deletes the all documents with the particular name 
    print(dl.deleted_count) # gives the count of docs deleted
    
    ## for more modifiers in finding, we can refer to: https://www.codewithharry.com/blogpost/mongodb-cheatsheet/


    
