from rest_framework import serializers
from aircraft.models import Aircraft
from airline.models import Airline

class AircraftSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer_serial_number = serializers.CharField()
    type = serializers.CharField()
    model = serializers.CharField()
    operator_airline = serializers.PrimaryKeyRelatedField(queryset=Airline.objects.all())
    number_of_engines = serializers.IntegerField()

    def validate_number_of_engines(self, value):
        if value < 1:
            raise serializers.ValidationError("Motor sayısı 1 den küçük olamaz.")
        return value

    def create(self, validated_data):
        return Aircraft.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer_serial_number = validated_data.get('manufacturer_serial_number', instance.manufacturer_serial_number)
        instance.type = validated_data.get('type', instance.type)
        instance.model = validated_data.get('model', instance.model)
        instance.operator_airline = validated_data.get('operator_airline', instance.operator_airline)
        instance.number_of_engines = validated_data.get('number_of_engines', instance.number_of_engines)
        instance.save()
        return instance