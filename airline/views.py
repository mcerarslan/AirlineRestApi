from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render


from airline.models import Airline
from airline.serializer import AirlineSerializer

@api_view(['GET','POST'])
def airlines(request):
    if request.method == "GET":
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines,many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = AirlineSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def airline(request,id):
    try:
       airline = Airline.objects.get(pk=id)

    except:
       return Response({"error": "Eşleşen bir kayıt bulunamadı."}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
       serializer = AirlineSerializer(airline)
       return Response(serializer.data, status= status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = AirlineSerializer(airline, data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        serializer = AirlineSerializer(airline, data = request.data, partial=True)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        airline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

