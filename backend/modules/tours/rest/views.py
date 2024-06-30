from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from modules.tours.models import TourInstance
from modules.tours.rest.serializers import TourInstanceSerializer, AvailabilitySerializer


class TourInstanceViewSet(viewsets.ModelViewSet):
    queryset = TourInstance.objects.all()
    serializer_class = TourInstanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post'], detail=True, serializer_class=AvailabilitySerializer)
    def is_available(self, request, pk=None):
        tour_instance = self.get_object()
        serializer = self.get_serializer(data=request.data, context={'tour_instance': tour_instance})
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_200_OK)
