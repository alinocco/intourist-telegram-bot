from rest_framework import permissions, viewsets

from modules.signups.models import TouristSignup
from modules.signups.rest.serializers import TouristSignupSerializer


class TouristSignupViewSet(viewsets.ModelViewSet):
    queryset = TouristSignup.objects.all()
    serializer_class = TouristSignupSerializer
    permission_classes = [permissions.IsAuthenticated]
