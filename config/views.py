from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!!")

def pybo_index(request):
    return HttpResponse("This is pybo application.")