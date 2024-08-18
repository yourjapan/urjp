
from django.db import models
from django.db.models import Model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


# ______________________________________________________________________________
# Item

class Item(Model):
    SKU = models.CharField(unique=True, max_length=255)
    n = models.IntegerField()

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    imports = serializers.SerializerMethodField()
    exports = serializers.SerializerMethodField()
    
    def get_imports(self, o):
        return sum(imp.n for imp in o.imports.all())
    
    def get_exports(self, o):
        return sum(exp.n for exp in o.exports.all())


# ______________________________________________________________________________
# Import

class Import(Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='imports')
    n = models.IntegerField()

class ImportSerializer(ModelSerializer):
    class Meta:
        model = Import
        fields = '__all__'
    item = serializers.SlugRelatedField(queryset=Item.objects, slug_field='SKU')


# ______________________________________________________________________________
# Export

class Export(Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='exports')
    n = models.IntegerField()

class ExportSerializer(ModelSerializer):
    class Meta:
        model = Export
        fields = '__all__'
    item = serializers.SlugRelatedField(queryset=Item.objects, slug_field='SKU')
