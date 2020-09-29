import datetime
from rest_framework.response import Response
from rest_framework.status import * 
from rest_framework.decorators import api_view
import rest_framework.exceptions as req_err
from .services import mongoclient
import json


db = mongoclient()

order_docs = {}
cost_center_docs = {}
customer_docs = {}
product_docs = {}
supplier_docs = {}

@api_view()
def orders(request):
    id_get = request.GET.get('_id')
    
    try:
        if request.method == 'GET' and id_get:
            for doc in db['orders'].find():
                order_docs.add(doc)

            return Response(json.dumps(order_docs), content_type='application/json')
        
        elif request.method == 'POST' or request.PUT.put('_id'):
            id_put = request.PUT.put('_id')
            data = json.loads(request.body)
            db['orders'].update_one({'_id': id_put}, data)

            return Response(json.dumps({'updated', db.orders.find({'_id':id_put})}), content_type='application/json')
        
        elif request.method == 'DELETE' and request.DELETE.delete('_id'):
            id_del = request.DELETE.delete('_id')
            del_sum = db
            db['orders'].drop_one({'_id':id_del})

            return Response(json.dumps({'msg':'removed', 'del_count': 1}), content_type='application/json')
    
    except (Exception) as e:
        return Response(json.dumps({'error': 'Invalid request: {0}'.format(str(e))}), status=HTTP_400_BAD_REQUEST, content_type='application/json')

@api_view()
def cost_centers(request):
    for doc in db['CostCenters'].find():
        cost_center_docs.add(doc)

    return Response(json.JSONEncoder(cost_center_docs))

@api_view()
def customers(request):
    for doc in db['Customers'].find():
        customer_docs.add(doc)
    
    return Response(json.JSONEncoder(customer_docs))

@api_view()
def products(request):
    for doc in db['Products'].find():
        product_docs.add(doc)

    return Response(json.JSONEncoder(pro))

@api_view()
def suppliers(request):
    for doc in db['Suppliers'].find():
        supplier_docs.add(doc)

    return Response(json.JSONEncoder(supplier_docs))