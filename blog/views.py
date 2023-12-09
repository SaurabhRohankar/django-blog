from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'title': 'Blog 1',
        'author': 'Saura',
        'blog_content': 'This is FIRST blog',
        'date_posted': '3 Dec 2023'
    },
    {
        'title': 'Blog 2',
        'author': 'Saurabh',
        'blog_content': 'This is SECOND blog',
        'date_posted': '4 Dec 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
