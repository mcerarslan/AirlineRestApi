from django.http import JsonResponse
from django.shortcuts import render

from airline.models import Airline

def airline_list(request):
    airline = Airline.objects.all()
    airline_list = list(airline.values())
    return JsonResponse({
        "airlines" : airline_list
    })

def create(request):
    pass


