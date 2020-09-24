from django.shortcuts import render
from rest_framework_mongoengine import viewsets
import datetime
from .services import RemoteMongoClient
from .serializers import *
from rest_framework.response import Response
from .models import *

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()