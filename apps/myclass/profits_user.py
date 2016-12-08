from django.http import HttpResponse

def test(request,name):

    return HttpResponse(r'hello i am profits '+name+' is you ?')