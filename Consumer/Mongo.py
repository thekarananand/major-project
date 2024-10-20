import pymongo

# Create/Access MongoClient to connect to Mongo Container
mongo_container = pymongo.MongoClient( 'mongo' , 27017 )

# Create/Access DB named minor-project
db_minor_project = mongo_container["major-project"]

# Create/Access Collection named data_log
data_log = db_minor_project["data-log"]


def save( Dict ):
    x = data_log.insert_one( Dict )