from django.http import HttpResponse

def test(request):
    return HttpResponse(r'hello i am profits')