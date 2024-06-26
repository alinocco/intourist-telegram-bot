from rest_framework import serializers

from modules.tours.models import TourInstance, Tour


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class TourInstanceSerializer(serializers.ModelSerializer):
    tour = TourSerializer()

    class Meta:
        model = TourInstance
        fields = '__all__'
