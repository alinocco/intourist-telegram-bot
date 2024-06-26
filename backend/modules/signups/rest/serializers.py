from rest_framework import serializers

from modules.signups.models import TouristSignup


class TouristSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristSignup
        fields = '__all__'
