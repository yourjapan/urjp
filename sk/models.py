
from django.db import models
from django.db.models import Model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class Item(Model):
    SKU = models.CharField(unique=True, max_length=255)

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
