from django.http import HttpResponseRedirect
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *
from .models import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CarMarkViewSet(viewsets.ModelViewSet):
    queryset = CarMark.objects.all()
    serializer_class = CarMarkSerializers


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializers
