# Generated by Django 4.2.8 on 2023-12-31 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_statistics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistics',
            old_name='totalstudent_in_word',
            new_name='totalstudent_in_words',
        ),
    ]
