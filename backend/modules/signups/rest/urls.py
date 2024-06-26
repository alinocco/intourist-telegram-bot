from django.urls import include, path
from rest_framework import routers

from modules.signups.rest import views

router = routers.DefaultRouter()
router.register(r'signups', views.TouristSignupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
