from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView

# Create your views here.

def newpost(request):
    if request.method=='POST':
        f=PostForm(request.POST)
        new_post=f.save()

        return redirect('/')
    else:
        f=PostForm()

    return render(request, 'report/post.html', {'form':f})


def home(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, 'report/home.html', context)

post_detail = DetailView.as_view(model=Post)