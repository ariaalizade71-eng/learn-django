from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def http_test(requests):
    return HttpResponse('<h1> this is a test </h1>')

def json_test(requests):
    return JsonResponse({'aria' : 19 , 'ali' : 18})
