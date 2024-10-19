from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class CarMark(models.Model):
    car_mark_name = models.CharField(max_length=100)

    def __str__(self):
        return self.car_mark_name


class CarModel(models.Model):
    car_model_name = models.CharField(max_length=100)

    def __str__(self):
        return self.car_model_name
