from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required(login_url='login')
def home_view(request):
    posts = Post.objects.all()
    print(request)

    return render(request, 'home/index.html', {
        'posts': posts
    })