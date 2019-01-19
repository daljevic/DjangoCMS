from django.shortcuts import render

posts = [
    {
        'author': 'Alex',
        'title': 'First blog post',
        'content': 'My First content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Marko',
        'title': 'Second blog post',
        'content': 'My Second content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
