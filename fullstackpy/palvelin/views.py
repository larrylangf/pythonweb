from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from .models import Currency
import requests
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication

@api_view()
@permission_classes([permissions.IsAdminUser])
def CallApiView(request):
    url = 'http://data.fixer.io/api/latest?access_key=2abd8709720df12e08596d320985579c'

    r = requests.get(url = url) 
    data = r.json()
    for key, value in data['rates'].items():
        Currency.objects.create(name=key, rate=value)
      
    return Response('luotu')

class CurrencyView(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

@api_view()
@permission_classes([permissions.IsAdminUser])
def DeleteView(request):
    currencies = Currency.objects.all()
    queryset = currencies.delete()
    return Response('Poisettu')


class UserView(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = UserSerializer
    queryset = User.objects.all()

@api_view()
@permission_classes([permissions.AllowAny])
def UserLogout(request):
    request.session.delete()
    return Response('Kirjattu ulos')

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def getCurrencies(request):
    queryset = Currency.objects.all()
    serializer = CurrencySerializer(queryset, many=True)
    return Response(serializer.data)