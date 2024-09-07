
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from ..models import *


class EbayViewSet(ViewSet):

    @action(methods=['post'], detail=False)
    def order(self, r):
        try:
            export = ExportSerializer(data=r.data)
            export.is_valid(raise_exception=True)
            export.save()
        finally:
            return Response()
