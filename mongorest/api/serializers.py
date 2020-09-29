'''
from rest_framework_mongoengine import serializers
from .models import *

class OrderSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CustomerSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SupplierSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class CostCenterSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CostCenter
        fields = '__all__'
'''