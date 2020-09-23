from rest_framework_mongoengine import serializers

class CustomerSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Product
        fields = '__all__'