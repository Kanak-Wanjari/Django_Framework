from django.shortcuts import render,HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("shop websites")