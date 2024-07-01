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


class AvailabilitySerializer(serializers.Serializer):
    people_quantity = serializers.IntegerField()

    def validate_people_quantity(self, value):
        tour_instance = self.context['tour_instance']
        # TODO: return how many available.
        if not tour_instance.is_available(value):
            raise serializers.ValidationError(
                f'Tour is not available for {value} people.'
            )
        return value
