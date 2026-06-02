from django.shortcuts import render

def home_view(requests):
    return render (requests , 'blog/blog-home.html')

def single_view(requests):
    return render (requests , 'blog/blog-single.html')
