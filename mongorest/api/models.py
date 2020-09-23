# from django.db import models
from mongoengine import Document, EmbeddedDocument, fields
import datetime

# MongoDB Documents

class Customer(Document):
    name = fields.StringField
    notification_email = fields.EmailField(allow_utf8_user=True, null=True)
    orders = fields.ListField(fields.EmbeddedDocument(Order))
    costcenters = fields.ListField(fields.EmbeddedDocument(CostCenter))

class Order(Document):
    order_date = fields.DateTimeField(default=datetime.date.now())
    delivery_address = fields.StringField


class Product(Document):
    unit = fields.StringField
    display_name = fields.StringField
    suppliers = fileds.ListField(fields.EmbeddedDocument(Supplier))


class CostCenter(Document):
    name = fields.StringField
    billing_address = fields.StringField

class Supplier(Document):
    name = fields.StringField
    customers = fields.ListField(fields.EmbeddedDocument(Customer))