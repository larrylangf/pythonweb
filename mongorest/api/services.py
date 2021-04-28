# api service modules
import os
import datetime
import pymongo
import dotenv
import mandrill
from requests_oauthlib import OAuth1Session
import requests
from base64 import b64encode, b64decode


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
    return t.strftime('%d.%m.%Y %H:%M:%S')

def mandrillclient():
    try:
        key = os.getenv('MANDRILLAPI_KEY')
        client = mandrill.Mandrill(key)
        return client
    except (mandrill.Error, Exception) as e:
        return print (f'error: {e.__class__} - {e}')


def send_subscribe_mail(r):
    try:
        c = mandrillclient()
        t = ftstamp()
        result = c.messages.send_raw(
            raw_message='''Subject: test mail\n\nSome content. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Donec vel felis id nisl sagittis faucibus nec nec libero 
            Nullam aliquam venenatis risus, vel vehicula libero viverra id.''', 
            from_email=email, from_name=user, to=to, ip_pool='Main Pool', send_at=t.split()[0], 
            return_path_domain=None)
        return print('success')

    except (mandrill.Error, Exception) as e:
        return print(f'error: {e.__class__} - {e}')


def getawayapisms(sender: str, msg: str, recipients: list):
    try:
        key = os.getenv('GETAWAYAPI_KEY')
        secret = b64encode(key.encode('ascii'))
        data = {
            "sender": sender,
            "message": msg,
            "recipients": [
                {"msisdn": num.zfill(len(num))}
                for num in recipients
            ],
        }
        resp = requests.post(
            "https://gatewayapi.com/rest/mtsms",
            json=data,
            auth=(key, ''),
        )
        return print(resp.json(),'\n',resp.raise_for_status())

    except Exception as e:
        return print(e)