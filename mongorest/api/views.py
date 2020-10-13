from django.http import JsonResponse
import rest_framework.exceptions as rest_err 
import datetime
import json
import requests
import pymongo
from decouple import config
from bson import json_util, objectid


user = config('MONGO_U')
password = config('MONGO_S')
host = config('MONGO_HOST')
db_name = config('DB_NAME')

try: 
    url = f'mongodb://{user}:{password}@{host}:27017/{db_name}?authSource=admin&readPreference=primary&ssl=false&authMechanism=SCRAM-SHA-1'
    client = pymongo.MongoClient(url, document_class=dict)
    db = client[f'{db_name}']
    print(f"connected to {client}")
        
except (pymongo.errors.ConnectionFailure, Exception) as e:
    print(f'Server not avaible \n {e}')


def amounts(request):
    col = db.amounts
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)

        elif request.method != 'DELETE':
            data = json.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                reqs.append(pymongo.UpdateOne({'_id': objectid.ObjectId(str(id_put))}, {"$set": data}))
            else:
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count}, safe=False)
    
    except rest_err.bad_request as e:
        return JsonResponse({'error': f'bad request: {e}'}, status=400)


def addresses(request):
    col = db.addresses
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)

        elif request.method != 'DELETE':
            data = json.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                reqs.append(pymongo.UpdateOne({'_id': objectid.ObjectId(str(id_put))}, {"$set": data}))
            else:
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count}, safe=False)    

    except rest_err.bad_request as e:
        return JsonResponse({'error': f'bad request: {e}'})


def cost_centers(request):
    col = db.cost_centers
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)
        
        elif request.method != 'DELETE':
            data = json.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                reqs.append(pymongo.UpdateOne({'_id': objectid.ObjectId(str(id_put))}, {"$set": data}))
            else:
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count}, safe=False)

    except (Exception) as e:
        return JsonResponse({'error': f'Invalid request: {e}'})


def customers(request):
    col = col.find({})
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)
        
        elif request.method != 'DELETE':
            data = json.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                reqs.append(pymongo.UpdateOne({'_id': objectod.ObjectId(str(id_put))}, {"$set": data}))
            else:
                reqs.append(pymongo.InsertOne(data))

            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id':ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count}, safe=False)

    except Exception as e:    
        return JsonResponse({'error': f'Invalid request: {e}'})


def products(request):
    col = db.products
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)
        
        elif request.method != 'DELETE':
            data = json.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                reqs.append(pymongo.UpdateOne({'_id': objectid.ObjectId(str(id_put))}, {"$set": data}))
            else:
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count}, safe=False)

    except Exception as e:
        return JsonResponse({'error': f'Invalid request: {e}'})    



def suppliers(request):
    col = db.suppliers
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)
        
        elif request.method != 'DELETE':
            data = json.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                reqs.append(pymongo.UpdateOne({'_id': objectid.ObjectId(str(id_put))}, {"$set": data}))
            else:
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id':ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count}, safe=False)

    except Exception as e:
        return JsonResponse({'error': f'Invalid request: {e}'})


def orders(request):
    col = db.orders
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)
        
        elif request.method != 'DELETE':
            data = json.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                reqs.append(pymongo.UpdateOne({'_id': objectid.ObjectId(str(id_put))}, {"$set": data}))
            else:
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count}, safe=False)

    except (Exception) as e:
        return JsonResponse({'error': f'Invalid request: {e}'}, status=400)


def delivery_locations(request):
    col = db.delivery_locations
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find({})))), safe=False)

        elif request.method != 'DELETE':
            data = json.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                reqs.append(pymongo.UpdateOne({'_id': objectid.ObjectId(str(id_put))}, {"$set": data}))
            else:
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
    
            return JsonResponse({'removed': q.deleted_count}, safe=False)
    
    except (Exception) as e:
        return JsonResponse({'error': f'Bad request: {e}'}, status=400)


client.close()