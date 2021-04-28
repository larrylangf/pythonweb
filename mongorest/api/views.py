from django.http import JsonResponse
import rest_framework.exceptions as rest_err 
import json
import pymongo
from bson import json_util, objectid, dbref
import api.services as funcs


db = funcs.connect_client()
z = datetime.timezone(datetime.timedelta(hours=2))
t = datetime.datetime.now(z)
ftime = funcs.ftstamp(t)

def amounts(request):
    col = db.amounts
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)

        elif request.method != 'DELETE':
            data = json_util.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            products = request.GET,get('products')
            if id_put:
                data.update({'updated_at': t})
                reqs.append(pymongo.ReplaceOne({'_id': objectid.ObjectId(str(id_put))}, data))
            else:
                data.update({'created_at': t})
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count})
    
    except rest_err.bad_request as e:
        return JsonResponse({'error': f'bad request: {e}'}, status=400)


def addresses(request):
    col = db.addresses
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)

        elif request.method != 'DELETE':
            data = json_util.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            dlocs = request.GET.get('delivery-locations')
            if id_put:
                data.update({'updated_at': t})
                reqs.append(pymongo.ReplaceOne({'_id': objectid.ObjectId(str(id_put))}, data))
            else:
                data.update({'created_at': t})
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count})    

    except rest_err.bad_request as e:
        return JsonResponse({'error': f'bad request: {e}'})


def cost_centers(request):
    col = db.cost_centers
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)
        
        elif request.method != 'DELETE':
            data = json_util.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                data.update({'updated_at': t})
                reqs.append(pymongo.ReplaceOne({'_id': objectid.ObjectId(str(id_put))}, data))
            else:
                data.update({'created_at': t})
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count})

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
                q = col.find_one({'_id': objectid.ObjectId(str(id_get))})
                return JsonResponse(json.loads(json_util.dumps(q)))
            else:
                return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)
        
        elif request.method != 'DELETE':
            data = json_util.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                data.update({'updated_at': t})
                reqs.append(pymongo.ReplaceOne({'_id': objectid.ObjectId(str(id_put))}, data))
            else:
                data.update({'created_at': t})
                reqs.append(pymongo.InsertOne(data))

            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count})

    except Exception as e:    
        return JsonResponse({'error': f'Invalid request: {e}'})


def products(request):
    col = db.products
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)
        
        elif request.method != 'DELETE':
            data = json_util.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                data.update({'updated_at': t})
                reqs.append(pymongo.ReplaceOne({'_id': objectid.ObjectId(str(id_put))}, data))
            else:
                data.update({'created_at': t})
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count})

    except Exception as e:
        return JsonResponse({'error': f'Invalid request: {e}'})    



def suppliers(request):
    col = db.suppliers
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            id_get = request.GET.get('id')
            if id_get:
                q = col.find_one({'_id': objectid.ObjectId(str(id_get))})
                return JsonResponse(json.loads(json_util.dumps(q)))
            else:
                return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)
        
        elif request.method != 'DELETE':
            data = json_util.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            if id_put:
                data.update({'updated_at': t})
                reqs.append(pymongo.ReplaceOne({'_id': objectid.ObjectId(str(id_put))}, data))
            else:
                data.update({'created_at': t})
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count})

    except Exception as e:
        return JsonResponse({'error': f'Invalid request: {e}'})


def orders(request):
    col = db.orders
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            id_get = request.GET.get('id')
            customers = request.GET.get('/customers')
            if id_get and customers:
                q = col.find_one({'customer': objectid.ObjectId(str(id_get))})
                return JsonResponse(json.loads(json_util.dumps(q)), safe=False)
            elif id_get:
                q = col.find_one({'_id': objectid.ObjectId(str(id_get))})
                return JsonResponse(json.loads(json_util.dumps(q)), safe=False)
            else:
                return JsonResponse(json.loads(json_util.dumps(list(col.find()))), safe=False)
        
        elif request.method != 'DELETE':
            data = json_util.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            customers = request.GET.get('customers')
            if id_put or customers:
                data.update({'updated_at': t})
                data.update({'customer': objectid.ObjectId(str(id_put))})
                reqs.append(pymongo.ReplaceOne({'_id': objectid.ObjectId(str(id_put))}, data))
            else:
                data.update({'order_date': t.split()[0], 'order_time': t.split()[1], 'created_at': t})
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
            
            return JsonResponse({'removed': q.deleted_count})

    except (Exception) as e:
        return JsonResponse({'error': f'Invalid request: {e}'}, status=400)


def companies(request):
    col = db.companies
    queryset = list(col.find({}))
    try:
        if request.method == 'GET':
            return JsonResponse(json.loads(json_util.dumps(list(col.find({})))), safe=False)

        elif request.method != 'DELETE':
            data = json_util.loads(request.body)
            reqs = []
            id_put = request.GET.get('id')
            t = datetime.datetime.now()
            if id_put:
                data.update({'updated_at': t})
                reqs.append(pymongo.ReplaceOne({'_id': objectid.ObjectId(str(id_put))}, data))
            else:
                data.update({'created_at': t})
                reqs.append(pymongo.InsertOne(data))
            q = col.bulk_write(reqs)

            return JsonResponse({'changed': q.modified_count, 'added': q.inserted_count})
        
        else:
            id_del = request.GET.get('id')
            q = col.delete_many({'_id': objectid.ObjectId(str(id_del))})
    
            return JsonResponse({'removed': q.deleted_count})
    
    except (Exception) as e:
        return JsonResponse({'error': f'Bad request: {e}'}, status=400)


db.client.close()