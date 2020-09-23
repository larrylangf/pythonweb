# connect remote machine to vm instance mongodb module
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url = "mongodb://os.qetenv(''):@/admin"
client = pymongo.MongoClient(url)