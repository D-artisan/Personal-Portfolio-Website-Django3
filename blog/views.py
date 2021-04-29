from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    return render(request, 'blog/home.html')

def all_blogs(request):
    posts = Post.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'posts': posts})

def detail(request, blog_id):
    blog = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
