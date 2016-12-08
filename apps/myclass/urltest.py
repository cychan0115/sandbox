from django.core.urlresolvers import LocaleRegexURLResolver
from django.conf.urls import patterns, url
from apps.myclass.profits_user import  test

def urltest(request):
    return [
        url(r'^(\d+)$',test),
    ]