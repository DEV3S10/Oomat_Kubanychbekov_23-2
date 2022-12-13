from django.shortcuts import render, HttpResponse, redirect
import datetime

# Create your views here.


def hello_world_view(request):
    return HttpResponse('HELLO WORLD!')


def datetime_view(request):
    return HttpResponse(datetime.datetime.now())


def goodbye_view(request):
    return HttpResponse('Goodbye user!')
