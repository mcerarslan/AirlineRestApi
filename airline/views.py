from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

from airline.models import Airline
from airline.serializer import AirlineSerializer

@api_view(['GET'])
def airline_list(request):
    airlines = Airline.objects.all()
    serializer = AirlineSerializer(airlines,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def airline_create(request):
    serializer = AirlineSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)



