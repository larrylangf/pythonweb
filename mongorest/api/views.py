from django.shortcuts import render
from rest_framework_mongoengine import viewsets
import datetime

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Tool.objects.all()