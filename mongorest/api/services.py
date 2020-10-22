# api service modules
import os
import datetime
import pymongo
import dotenv


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
        db = client[f'{db_name}']
        return db
        
    except (pymongo.errors.ConnectionFailure, Exception) as e:
        return print(f'Server not avaible \n{e}')
        

def ftstamp():
    z = datetime.timezone(datetime.timedelta(hours=2))
    t = datetime.datetime.now(z)
    return t.strftime('%d.%m.%Y %H:%M:%S')