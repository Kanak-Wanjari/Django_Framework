#I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("Removepunc")

def capfirst(request):
    return HttpResponse("CapItalize First")

def newlineremove(request):
    return HttpResponse("New Line Removed")

def spaceremove(request):
    return HttpResponse("Space removed")

def charcount(request):
    return HttpResponse("Character Count")