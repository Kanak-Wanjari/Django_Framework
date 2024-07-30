#I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    if removepunc == 'on':
        punctuations = '''!()-[]{;:}'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuation' , 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps == 'on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase' , 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremover == 'on'):
        analyzed=""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose':'New Line Removed' , 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    elif(extraspaceremover == 'on'):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Removed' , 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
# def capfirst(request):
#     return HttpResponse("CapItalize First")

# def newlineremove(request):
#     return HttpResponse("New Line Removed")

# def spaceremove(request):
#     return HttpResponse("Space removed")

# def charcount(request):
#     return HttpResponse("Character Count")