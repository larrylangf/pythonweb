''' 
from django.db import models
from mongoengine import *
import datetime

# MongoDB Documents

class Order(Document):
    order_date = DateTimeField(default=datetime.date)
    order_time = DateTimeField(default=datetime.time)
    delivery_address = StringField

class CostCenter(Document):
    name = StringField
    billing_address = StringField

class Customer(Document):
    name = StringField
    notification_email = EmailField(allow_utf8_user=True, null=True)
    orders = ListField(LazyReferenceField((Order), reverse_delete_rule=PULL))
    costcenters = ListField(LazyReferenceField((CostCenter), reverse_delete_rule=PULL))

class Product(Document):
    unit = StringField
    display_name = StringField

class Supplier(Document):
    name = StringField
    customers = ListField(LazyReferenceField((Customer), reverse_delete_rule=PULL))
    products = ListField(LazyReferenceField((Product), reverse_delete_rule=PULL))
    costcenters = ListField(LazyReferenceField((CostCenter), reverse_delete_rule=PULL))
'''