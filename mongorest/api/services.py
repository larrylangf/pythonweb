# module to connect remote mongoclient
import os
from dotenv import load_dotenv
import pymongo

load_dotenv()
host = os.getenv('VM_HOST')
user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASS')


def mongoclient():
    try: 
        url = 'mongodb://{user}:{password}@{host}:27017/?authSource=admin&readPreference=primary&ssl=false&authMechanism=SCRAM-SHA-1'
        client = pymongo.MongoClient(url)
        db = client['pymongo-api']
    except (pymongo.errors.ConnectionFailure, Exception) as e:
        return print('Server not avaible \n',e)
    else:
        return print("You are connected!"), db