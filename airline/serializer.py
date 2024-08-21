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
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.callsign = validated_data.get("callsign",instance.callsign)
        instance.founded_year = validated_data.get("founded_year",instance.founded_year)
        instance.base_airport = validated_data.get("base_airport",instance.base_airport)
        instance.save()
        return instance