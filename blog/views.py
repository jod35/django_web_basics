from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts=Post.objects.all()


def index(request):
    context = {
         'title':'Home',
        'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
	context={'title' : "About Page"}
	return render(request, 'blog/about.html',context)
