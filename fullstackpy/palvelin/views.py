from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import Currency
import requests
from django.contrib.auth.models import User
import os
from dotenv import dotenv_values
config = dotenv_values("../../.env")

@api_view()
def CallApiView(request):
    url = 'http://data.fixer.io/api/latest?access_key='+os.getenv('API_KEY')

    r = requests.get(url) 
    data = r.json()
    for key, value in data['rates'].items():
        Currency.objects.create(name=key, rate=value)
      
    return Response('Tiedot haettu API:sta')

class CurrencyView(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

@api_view()
def DeleteView(request):
    currencies = Currency.objects.all()
    queryset = currencies.delete()
    return Response('Paikallinen tietokanta tyhjennetty')

# kaikki käyttäjät
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

@api_view()
def UserLogout(request):
    request.session.delete()
    return Response('Kirjauduttu ulos')

# Vaihtoehtoinen tapa hakea lokaalin kantaan talletut valuuttakurssit
@api_view(['GET'])
def getCurrencies(request):
    queryset = Currency.objects.all()
    serializer = CurrencySerializer(queryset, many=True)
    return Response(serializer.data)