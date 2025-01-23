from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_world(request):
    return render(request, 'hello.html', {
        'name': 'Ibrahim'
    })

def show_article(request, id, slug):
    return render(request, 'article/show_article.html', {
        'title' : 'Article ' + str(id),
        'content': 'Article content ' + str(slug)
    })  
