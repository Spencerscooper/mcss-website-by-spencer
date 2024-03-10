from django.urls import path, include

from . import views

urlpatterns = [
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
    path('blog_signup', views.blog_signup, name='blog_signup'),
    path('blog_login', views.blog_login, name='blog_login'),
     path('blog_logout', views.blog_logout, name='blog_logout'),
    path('dashboard', views.dashboard, name='dashboard'),

    
]