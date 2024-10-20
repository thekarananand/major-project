import pymongo

# Create/Access MongoClient to connect to Mongo Container
mongo_container = pymongo.MongoClient( 'mongo' , 27017 )
# mongo_container = pymongo.MongoClient( 'localhost' , 80 )

# Create/Access DB named minor-project
db_minor_project = mongo_container["major-project"]

# Create/Access Collection named data_log
data_log = db_minor_project["data-log"]

def fetch():
    result = list(
        data_log.find(
            { "PV1": {"$gt": 0.5} },
            { "_id": 0 }
        ).sort("PV1", 1).limit(5)
    )
    
    return result