from django.shortcuts import get_object_or_404, render, redirect

from .forms import CommentForm
from .models import Post, Category

# Create your views here.
# This blog views.py will make it possible for  someone to view the post detail

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {'post':post, 'form':form })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category':category, 'posts': posts})
