# Generated by Django 4.2.8 on 2024-01-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_aboutmcss_image1_aboutmcss_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
