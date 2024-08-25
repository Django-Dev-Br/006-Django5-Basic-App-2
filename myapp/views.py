from django.http import HttpResponse

def status_view(request):
    return HttpResponse("app up and running properly")
