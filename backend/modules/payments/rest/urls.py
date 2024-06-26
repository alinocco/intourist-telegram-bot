from django.urls import include, path
from rest_framework import routers

from modules.payments.rest import views

router = routers.DefaultRouter()
router.register(r'payments', views.PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
