from django.shortcuts import render
from django.http import HttpResponse

def pybo_index(request):
    return HttpResponse("This is pybo application.")