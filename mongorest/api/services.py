# connect remote mongodb server
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pymongo

load_dotenv()
db_host = os.getenv('VM_HOST')
user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASS')
db = os.getenv('DB_NAME')

class RemoteMongoClient:
    try: 
        client = pymongo.MongoClient(
            host = db_host,
            port = 27017,
            username = user,
            password = password,
            authMechanism='SCRAM-SHA-1'
        )
    except (pymongo.errors.ConnectionFailure, Exception) as e:
        print('Server not avaible \n',e)
    else:
        print("You are connected!")
        return client