# Generated by Django 4.2.8 on 2024-03-16 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_rename_image_post_image3_post_image4_post_image5'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image1',
            new_name='image',
        ),
    ]
