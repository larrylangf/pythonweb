from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CurrencySerializer
from .models import Currency
import requests

@api_view()
def CallApiView(request):
    url = 'http://data.fixer.io/api/latest?access_key=2abd8709720df12e08596d320985579c'

    r = requests.get(url = url) 
    data = r.json()
    for key, value in data['rates'].items():
        Currency.objects.create(name=key, rate=value)
      
    return Response('luotu')


class CurrencyView(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

@api_view()
def DeleteView(request):
    currencies = Currency.objects.all()
    queryset = currencies.delete()
    return Response('poistettu')