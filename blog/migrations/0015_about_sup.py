# Generated by Django 4.2.8 on 2023-12-31 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_supe_goal'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_sup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('bio', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
    ]