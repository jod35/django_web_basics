from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Jonah',
        'title': 'Today in Tech',
        'content': 'CONTENT OF POST',
        'date_posted': '28th March'
    },
    {
        'author': 'Jonah',
        'title': 'Today in Tech',
        'content': 'CONTENT OF POST',
        'date_posted': '1st January'
    },
    {
        'author': 'Jonah',
        'title': 'Today in Tech',
        'content': 'CONTENT OF POST',
        'date_posted': '2nd February'
    },
]


def index(request):
    context = {
         'title':'Home',
        'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
	context={'title' : "About Page"}
	return render(request, 'blog/about.html',context)
