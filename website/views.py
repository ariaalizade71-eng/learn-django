from django.shortcuts import render
from django.http import HttpResponse


def index_view(requests):
    return render(requests , 'mytem/index.html')

def about_view(requests):
    return render(requests , 'mytem/about.html')

def contact_view(requests):
    return render(requests , 'mytem/contact.html')