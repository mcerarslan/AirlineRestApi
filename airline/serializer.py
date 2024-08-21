from rest_framework import serializers
from airline.models import Airline


class AirlineSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    callsign = serializers.CharField()
    founded_year = serializers.IntegerField()
    base_airport = serializers.CharField()

    def create(self,validated_data):
        return Airline.objects.create(**validated_data)