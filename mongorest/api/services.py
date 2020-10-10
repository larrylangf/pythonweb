# module to connect remote mongoclient
'''import pymongo
from decouple import config


user = config('MONGO_U')
password = config('MONGO_S')


def connect_client():
    try: 
        url = f'mongodb://{user}:{password}@mongodb.agendacloud.fi:27017/pymongo-api?authSource=admin&readPreference=primary&ssl=false&authMechanism=SCRAM-SHA-1'
        client = pymongo.MongoClient(url)

        return print("You are connected!"), client
        
    except (pymongo.errors.ConnectionFailure, Exception) as e:
        
        return print(f'Server not avaible \n {e}')'''
        
    
# for testing mongo connection & query results
# connect_client()