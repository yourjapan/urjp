
from rest_framework.routers import SimpleRouter
from rest_framework.viewsets import ModelViewSet
from .models import *


class ItemViewSet(ModelViewSet):
    queryset = Item.objects
    serializer_class = ItemSerializer


router = SimpleRouter()
router.register(r'items', ItemViewSet)
