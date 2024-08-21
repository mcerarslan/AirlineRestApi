from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render


from airline.models import Airline
from airline.serializer import AirlineSerializer

@api_view(['GET'])
def airline_list(request):
    airlines = Airline.objects.all()
    serializer = AirlineSerializer(airlines,many=True)
    return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['GET'])
def airline(request,id):
    try:
      airline = Airline.objects.get(pk=id)
      serializer = AirlineSerializer(airline)
      return Response(serializer.data, status= status.HTTP_200_OK)
    except:
       return Response({"error": "Eşleşen bir kayıt bulunamadı."}, status= status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def airline_create(request):
    serializer = AirlineSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def airline_update(request,id):
    airline = Airline.objects.get(pk=id)
    serializer = AirlineSerializer(airline, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def airline_patch(request,id):
    airline = Airline.objects.get(pk=id)
    serializer = AirlineSerializer(airline, data = request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def airline_delete(request,id):
    airline = Airline.objects.get(pk=id)
    airline.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

