# api service modules
import os
import datetime
import pymongo
import dotenv
import json
from bson import json_util, objectid

dotenv.load_dotenv()
user = os.getenv('MONGO_USER')
secret = os.getenv('MONGO_S')
host = os.getenv('MONGO_HOST')
db_name = os.getenv('DB_NAME')
ca_cert = os.path.realpath('ca.pem')
client_cert = os.path.realpath('mongodb.pem')

def connect_client():
    try: 
        url = f'mongodb://{user}:{secret}@{host}:27017/{db_name}?authSource=admin&authMechanism=SCRAM-SHA-256&tls=true&tlsCAFile={ca_cert}&tlsCertificateKeyFile={client_cert}'
        client = pymongo.MongoClient(url, document_class=dict)
        return print(f'connected \n{client}'), client
        
    except (pymongo.errors.ConnectionFailure, Exception) as e:
        return print(f'Server not avaible \n{e}')
        
def print_path():
    return print()

def fdatetime():
    d = datetime.date.today()
    t = datetime.datetime.now()
    return print(t)
    
def mongo_dbref():
    client = connect_client()
    db = client[f'{db_name}']
    # list(db.customers.find({})),'\n', list(db.orders.find({}))
    # db.orders.find({'customers._id': objectid.ObjectId('')})
    return print(list(db.amounts.find({})))

# for testing service func results
# mongo_dbref()
# print_path()
fdatetime()