
from rest_framework.routers import SimpleRouter
from rest_framework.viewsets import ModelViewSet
from .models import *


# ______________________________________________________________________________
# Item

class ItemViewSet(ModelViewSet):
    queryset = Item.objects
    serializer_class = ItemSerializer


# ______________________________________________________________________________
# Import

class ImportViewSet(ModelViewSet):
    queryset = Import.objects
    serializer_class = ImportSerializer


# ______________________________________________________________________________
# Export

class ExportViewSet(ModelViewSet):
    queryset = Export.objects
    serializer_class = ExportSerializer


# ______________________________________________________________________________
# Router

from .eb.eb import EbayViewSet


router = SimpleRouter()
router.register(r'items', ItemViewSet)
router.register(r'imports', ImportViewSet)
router.register(r'exports', ExportViewSet)
router.register(r'eb', EbayViewSet, basename='eb')
