from .sitemaps import CategorySitemap, PostSitemap 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap




from django.contrib import admin
from django.urls import path, include
from core.views import frontpage, about, administration, tubmanhigh_index, tubmanhigh_about, tubmanhigh_event, robots_txt
sitemaps = {'category' : CategorySitemap, 'post':PostSitemap}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('administration/', administration, name='administration'),
    # Tubman High School App urls
    path('tubmanhigh_index/', tubmanhigh_index, name='tubmanhigh_index'),
    path('tubmanhigh_about/', tubmanhigh_about, name='tubmanhigh_about'),
    path('tubmanhigh_event/', tubmanhigh_event, name='tubmanhigh_event'),

    path('', include('blog.urls')),
    path('', frontpage, name='frontpage'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'MCSS Site Administrator'
admin.site.site_title = 'MCSS Admin'
admin.site.index_title = 'Please ask Spencer before deleting anything!!!'
