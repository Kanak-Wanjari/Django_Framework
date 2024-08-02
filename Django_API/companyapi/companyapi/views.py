from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("Home Page Requested")
    friends = [
        'kanak',
        'Naruto',
        'Sasuke'
    ]
    return JsonResponse(friends, safe=False)