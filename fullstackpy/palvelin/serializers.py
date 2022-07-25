from rest_framework import serializers
from .models import Currency
from django.contrib.auth.models import User
# Tietokannan suodatus luokat
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'rate')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'is_superuser')