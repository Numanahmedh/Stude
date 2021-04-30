# Generated by Django 3.1.3 on 2021-01-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=5000)),
                ('image', models.ImageField(upload_to='blog_images')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
