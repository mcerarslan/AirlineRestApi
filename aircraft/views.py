from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from aircraft.models import Aircraft
from aircraft.serializer import AircraftSerializer

@api_view(['GET', 'POST'])
def aircrafts(request):
    if request.method == "GET":
        aircrafts = Aircraft.objects.all()
        serializer = AircraftSerializer(aircrafts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = AircraftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def aircraft(request, id):
    try:
        aircraft = Aircraft.objects.get(pk=id)
    except Aircraft.DoesNotExist:
        return Response({"error": "Eşleşen bir kayıt bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AircraftSerializer(aircraft)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = AircraftSerializer(aircraft, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        serializer = AircraftSerializer(aircraft, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        aircraft.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)