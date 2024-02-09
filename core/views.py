# core views.py with contain the function base view for my front pages
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post, Elementary_Galleries, JuniorHigh_Galleries, SeniorHigh_Galleries,School_fee, Honor_roll, Statistics, Aboutmcss, Formersups, Supe_goal, About_sup, Sr_Management, Council, tubmanhigh_admin
from django.core.paginator import Paginator
# Create your views here.

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page')
    post_obj = paginator.get_page(page_number)

    elementary_galleries = Elementary_Galleries.objects.all()
    juniorhigh_galleries = JuniorHigh_Galleries.objects.all()
    seniorhigh_galleries = SeniorHigh_Galleries.objects.all()
    tuition = School_fee.objects.all()
    dux_inform = Honor_roll.objects.all()
    statistic = Statistics.objects.all()

    return render(request, 'core/index.html', {'posts':post_obj, 'elementary_gallaries':elementary_galleries,
    'juniorhigh_gallaries':juniorhigh_galleries,'seniorhigh_galleries': seniorhigh_galleries,
    'tuition': tuition, 'dux':dux_inform, 'statistic':statistic})

def about(request):
    history = Aboutmcss.objects.all()
    past_sup = Formersups.objects.all()
    super_goal = Supe_goal.objects.all()
    supe_bio = About_sup.objects.all()
    return render(request, 'core/about.html',{'history': history,
    'past_sup': past_sup, 'super_goal':super_goal, 'supe_bio': supe_bio})

def administration(request):
    faculty = Sr_Management.objects.all()
    council = Council.objects.all()
    return render(request, 'core/administration.html', {'faculty': faculty, 'council': council })

#This section is for William V.S. Tubman High School 
def tubmanhigh_index(request):
 
    return render(request, 'core/Tubmanhigh/index.html',) 

def tubmanhigh_about(request):
    tubman_admin = tubmanhigh_admin.objects.all()
 
    return render(request, 'core/Tubmanhigh/about.html',{'tubman_admin': tubman_admin })

def tubmanhigh_event(request):
 
    return render(request, 'core/Tubmanhigh/events.html',)

#This end



def robots_txt(request):
    text = [
        "User-Agent: * ",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
