# Generated by Django 4.2.8 on 2023-12-31 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_formersups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supe_goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField()),
            ],
        ),
    ]