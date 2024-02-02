from django.db import models


# Create your models here.
# This blog models is intended to send information from the backend to the front page in core app


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

#This section contain all school images 

class Elementary_Galleries(models.Model):
    school_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

class JuniorHigh_Galleries(models.Model):
    school_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

class SeniorHigh_Galleries(models.Model):
    school_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)


#This section contain School fees inform on the index page
    

class School_fee(models.Model):
    division = models.CharField(max_length=100)
    tuition = models.DecimalField(max_digits=10, decimal_places=2)  # max_digits and decimal_places define the precision
    year = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.division} - ${self.tuition}"

#This section hold students who Dux our schools
class Honor_roll(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    school = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    year = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.school} {self.student_name}"

#This section contain MCSS Statistics/Enrollment record
class Statistics(models.Model):
    year = models.CharField(max_length=30)
    totalschool_in_words = models.CharField(max_length=100)
    totalschool_in_num = models.IntegerField()
    totalstudent_in_words = models.CharField(max_length=100)
    totalstudent_in_num = models.IntegerField()
    year_of_service_in_word = models.CharField(max_length=100)
    year_of_service_in_num = models.IntegerField()
    total_alumni_in_word = models.CharField(max_length=100)
    total_alumi_in_num = models.IntegerField()

#About Us Section 
class Aboutmcss(models.Model):
     body = models.TextField()
     image = models.ImageField(upload_to='uploads/', blank=True, null=True)
     image1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
     image2 = models.ImageField(upload_to='uploads/', blank=True, null=True)

class Formersups(models.Model):
    about = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name 

class Supe_goal(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()

class About_sup(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

#Senior Management
class Sr_Management(models.Model):
    name = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name

class Council(models.Model):
    name = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)












