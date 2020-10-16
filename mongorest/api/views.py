from django.http import JsonResponse
import rest_framework.exceptions as rest_err 
import datetime
import json
from bson import json_util, objectid, dbref
import api.services as funcs


client = funcs.connect_client()
db = client['pymongo-api']


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
    col = db.customers
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            id_get = request.GET.get('id')
            orders = request.GET.get('orders')
            if id_get:
                q = col.find_one({'_id': objectid.ObjectId(id_get)})
                return JsonResponse(json.loads(json_util.dumps()))
            else:
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
            id_get = request.GET.get('id')
            customers = request.GET.get('customers')
            if id_get and customers:
                q = col.find({'customers._id': objectid.ObjectId(str(id_get))})
                return JsonResponse(json.loads(json_util.dumps(list(q))))
            elif id_get:
                q = col.find_one({'_id': objectid.ObjectId(str(id_get))})
            else:
                return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)
        
        elif request.method != 'DELETE':
            data = json.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            t = datetime.datetime.now()
            if id_put:
                reqs.append(pymongo.UpdateOne({'_id': objectid.ObjectId(str(id_put))}, {"$set": data}))
            else:
                d = datetime.date.today()
                data.update({'order_date': d.strftime('%d.%m.%Y'), 'order_time': t.strftime('%H:%M:%S')})
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


def companies(request):
    col = db.companies
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find({})))))

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
    
            return JsonResponse({'removed': q.deleted_count})
    
    except (Exception) as e:
        return JsonResponse({'error': f'Bad request: {e}'}, status=400)


client.close()