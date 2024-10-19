from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CarMarkSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarMark
        fields = ['car_mark_name']


class CarModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['car_model_name']



