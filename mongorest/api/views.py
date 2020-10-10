import datetime
# from rest_framework.response import Response
from django.http import JsonResponse
# from rest_framework.status import *
import json
import pymongo
from decouple import config


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


amount_docs = {}
address_docs = {}
cost_center_docs = {}
customer_docs = {}
product_docs = {}
supplier_docs = {}
order_docs = {}
delivery_location_docs = {}


def amounts(request):
    try:
        if request.method == 'GET':
            docs = db['amounts'].find({})
            for c in docs.raw:
                amount_docs.update(bsonjs.dumps(c))
            
            return JsonResponse(amount_docs)

        elif request.method == 'POST':
            data = bsonjs.loads(request.body)
            q = db['amounts'].insert_one(RawBSONDocument(data))

            return JsonResponse({'added'})

        elif request.method == 'PUT':
            data = bsonjs.loads(request.body)
            q = db['amounts'].update_one({'_id':request.GET.get('id')}, RawBSONDocument(data))
        
            return JsonResponse({'updated': q.updated_count()})

        else:
            q = db['amounts'].delete_one({'_id':request.GET.get('id')})
        
            return JsonResponse({'deleted', q.deleted_count()})
    
    except (Exception) as e:

        queryset = list(db['amounts'].find({}))

        return JsonResponse({'error': f'Invalid request: {e}'})


def addresses(request):
    try:
        if request.method == 'GET':
            docs = db['addresses'].find({})
            for c in docs.raw:
                address_docs.update(bsonjs.dumps(c))
            
            return JsonResponse(address_docs)

        elif request.method == 'POST':
                data = bsonjs.loads(request.body)
                q = db['addresses'].insert_one(RawBSONDocument(data))

                return JsonResponse({'added'})

        elif request.method == 'PUT':
            data = bsonjs.loads(request.body)
            q = db['addresses'].update_one({'_id': request.GET.get('id')}, RawBSONDocument(data))

            return JsonResponse({'updated': q.updated_count()})
        
        elif request.method == 'DELETE':
            id_del = request.GET.get('id')
            q = db['addresses'].delete_one({'_id': id_del})
            
            return JsonResponse({'deleted', q.deleted_count()})    

    except (Exception) as e:

        queryset = list(db['addresses'].find({}))

        return JsonResponse({'error': f'Invalid request: {e}'})


def cost_centers(request):
    try:
        if request.method == 'GET':
            docs = db['cost-centers'].find({})
            for doc in docs.raw:
                cost_center_docs.add(bsonjs.dumps(doc))

            return JsonResponse(cost_center_docs)
        
        elif request.method == 'POST':
            data = bsonjs.loads(request.body)
            q = db['cost-centers'].insert_one(RawBSONDocument(data))

            return JsonResponse({'added': q.inserted_count()})

        elif request.method == 'PUT':
            data = bsonjs.loads(request.body)
            q = db['cost-centers'].update_one({'_id':request.POST.get('_id')}, RawBSONDocument(data))

            return JsonResponse({'updated': q.updated_count()})
        
        elif request.method == 'DELETE':
            q = db['cost-centers'].delete_one({'_id':request.GET.get('id')})
        
            return JsonResponse({'deleted', q.deleted_count()})

    except (Exception) as e:

        queryset = list(db['cost-centers'].find({}))
        return JsonResponse({'error': f'Invalid request: {e}'})


def customers(request):
    try:
        if request.method == 'GET':
            docs = db['customers'].find({})
            for doc in docs.raw:
                customer_docs.add(bsonjs.dumps(doc))

            return JsonResponse(customer_docs)
        
        elif request.method == 'POST':
            data = bsonjs.loads(request.body)
            q = db['customers'].insert_one(RawBSONDocument(data))

            return JsonResponse({'added': q.inserted_count()})

        elif request.method == 'PUT':
            data = bsonjs.loads(request.body)
            q = db['customers'].update_one({'_id':request.POST.get('_id')}, RawBSONDocument(data))

            return JsonResponse({'updated': q.updated_count()})

        elif request.method == 'DELETE':
            if request.GET.get('id'):
                c = db['customers'].delete_one({'_id':request.GET.get('id')})
            
            else:
                data = bsonjs.loads(request.body)
                c = db['customers'].delete_many(RawBSONDocument(data))
            
            return JsonResponse({'deleted': c.deleted_count()})

    except Exception as e:    
        
        queryset = list(db['customers'].find({}))

        return JsonResponse({'error': f'Invalid request: {e}'})


def products(request):
    try:
        if request.method == 'GET':
            docs = db['products'].find({})
            for doc in docs.raw:
                product_docs.add(bsonjs.dumps(doc))

            return JsonResponse(product_docs)
        
        elif request.method != 'DELETE':
            data = json.loads(request.body)
            q = db['products'].find_one_and_update({'_id':data['_id']}, {RawBSONDocument(data)}, upsert=True)
        
        else:
            q = db['products'].delete_one({'_id': request.GET.get('id')})

            return JsonResponse({'msg':'removed', 'del_count': q.deleted_count()})

    except Exception as e:

        queryset = list(db['products'].find({}))

        return JsonResponse({'error': f'Invalid request: {e}'})    



def suppliers(request):
    try:
        if request.method == 'GET':
            docs = db['suppliers'].find({})
            for doc in docs.raw:
                supplier_docs.add(bsonjs.dumps(doc))

            return print(supplier_docs)
        
        elif request.method != 'DELETE':
            data = bsonjs.loads(request.body)
            q = db['suppliers'].find_one_and_update({'_id':data['_id']}, {RawBSONDocument(data)}, upsert=True)
        
            return JsonResponse({'updated count': q.updated_count()})

        else:
            q = db['suppliers'].delete_one({'_id': request.GET.get('id')})

            return JsonResponse({'msg':'removed', 'del_count': q.deleted_count()})


    except Exception as e:

        queryset = list(db['suppliers'].find({}))

        return JsonResponse({'error': f'Invalid request: {e}'})


def orders(request):
    try:
        if request.method == 'GET':
            docs = db['orders'].find({})
            for doc in docs.raw:
                order_docs.add(bsonjs.dumps(doc))
            
            return JsonResponse(order_docs)
        
        elif request.method == 'POST':
            data = bsonjs.loads(request.body)
            q = db['orders'].insert_one(RawBSONDocument(data))

            return JsonResponse({'added'})

        elif request.method == 'PUT':
            data = bsonjs.loads(request.body)
            q = db['orders'].update_one({'_id':request.POST.get('_id')}, RawBSONDocument(data))

            return JsonResponse({'updated': q.updated_count()})
        
        elif request.method == 'DELETE':
            id_del = request.GET.get('_id')
            q = db['orders'].delete_one(bsonjs.loads({'_id':id_del}))
            
            return JsonResponse({'msg':'removed', 'del_count': q.deleted_count()})

    except (Exception) as e:

        queryset = list(db['orders'].find({}))

        return JsonResponse({'error': f'Invalid request: {e}'})


def delivery_locations(request):
    try:
        if request.method == 'GET':
            colls = db['delivery_locations'].find({})
            for doc in colls.raw:
                return print(bsonjs.dumps(doc))
        
        elif request.method == 'POST':
            data = bsonjs.loads(request.body)
            q = db['orders'].insert_one(RawBSONDocument(data))

            return JsonResponse({'added'})

        elif request.method == 'PUT':
            data = bsonjs.loads(request.body)
            q = db['delivery_locations'].update_one({'_id':request.POST.get('_id')}, data)

            return JsonResponse({'updated': q.modified_count()})
        
        elif request.method == 'DELETE':
            id_del = request.GET.get('id')
            q = db['delivery_locations'].delete_one({'_id':id_del})
            
            return JsonResponse({'msg':'removed', 'del_count': q.deleted_count()})
    
    except (Exception) as e:

        queryset = list(db['delivery_locations'].find({}))
        return JsonResponse({'error': f'Bad request: {e}'}, status=400)


client.close()