from django.urls import include, path
from rest_framework import routers

from modules.tours.rest import views

router = routers.DefaultRouter()
router.register(r'tours', views.TourInstanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
