from rest_framework import permissions, viewsets

from modules.payments.models import Payment
from modules.payments.rest.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
