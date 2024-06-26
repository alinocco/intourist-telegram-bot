from rest_framework import permissions, viewsets

from modules.tours.models import TourInstance
from modules.tours.rest.serializers import TourInstanceSerializer


class TourInstanceViewSet(viewsets.ModelViewSet):
    queryset = TourInstance.objects.all()
    serializer_class = TourInstanceSerializer
    permission_classes = [permissions.IsAuthenticated]
