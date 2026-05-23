from django.shortcuts import render
from django.http import HttpResponse


def index_view(requests):
    return HttpResponse('<h1> Home </h1>')

def about_view(requests):
    return HttpResponse('<h1> About </h1>')

def contact_view(requests):
    return HttpResponse('<h1> Contact </h1>')