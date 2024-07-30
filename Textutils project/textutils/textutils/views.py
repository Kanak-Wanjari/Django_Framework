#I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    analyzed = djtext
    params = {'purpose':'Removed Punctuation' , 'analyze_text':analyzed}
    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("CapItalize First")

# def newlineremove(request):
#     return HttpResponse("New Line Removed")

# def spaceremove(request):
#     return HttpResponse("Space removed")

# def charcount(request):
#     return HttpResponse("Character Count")