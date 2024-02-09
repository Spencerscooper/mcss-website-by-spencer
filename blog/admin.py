from django.contrib import admin

from .models import Post, Category, Comment, Elementary_Galleries ,JuniorHigh_Galleries, SeniorHigh_Galleries, School_fee, Honor_roll, Statistics, Aboutmcss, Formersups, Supe_goal, About_sup, Sr_Management, Council, tubmanhigh_admin

# Register your models here.
# This admin will contain the mdels from our blog app

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body',]
    list_display = ['title', 'slug', 'category','created_at', 'status']
    list_filter = ['category', 'created_at','status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug':('title',)}


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','post','created_at']
   


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
#This section hold the images for all schools
admin.site.register(Elementary_Galleries)
admin.site.register(JuniorHigh_Galleries)
admin.site.register(SeniorHigh_Galleries)

#PTA Fees or Tuition 
admin.site.register(School_fee)

#Honor Society
admin.site.register(Honor_roll)

#School Statistic
admin.site.register(Statistics)

#Aboutmcss
admin.site.register(Aboutmcss)

admin.site.register(Formersups)

admin.site.register(Supe_goal)

admin.site.register(About_sup)
admin.site.register(Sr_Management)
admin.site.register(Council)
admin.site.register(tubmanhigh_admin)

