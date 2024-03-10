from django.shortcuts import get_object_or_404, render, redirect
#Below are new code added
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from django.contrib import messages
from core import views
#end here


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

def blog_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Already Used')
                return redirect('blog_signup')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used!!')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('blog/blogregistration/blog_login.html')
        
        else:
            messages.info(request, 'Password Not The Same!!')
            return redirect('blog/blog_signup')
    
    else:
        return render(request, 'blog/blogregistration/blog_signup.html')
    
def blog_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        
        else:
            messages.info(request, 'Credential Invalid!!')
            return render(request, 'blog/blogregistration/blog_login.html')
    else:
        return render(request, 'blog/blogregistration/blog_login.html')

def blog_logout(request):
    auth.logout(request)
    return redirect('/')

def dashboard(request):

    return render(request, 'blog/blogregistration/dashboard.html')
    
 
        
