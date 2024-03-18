from django.shortcuts import render
from myapp.models import Post

# Create your views here.

def base(request):
    return render (request, 'myapp/base.html')

def post(request):

    posts = Post.objects.all()

    context = {
        'all_posts' : posts
    }

    return render(request, "myapp/index.html", context)

def detail(request,id):

    my_post = Post.objects.get(id=id)

    context = {
        'single_post' : my_post
    }

    return render(request, "myapp/detail.html", context)