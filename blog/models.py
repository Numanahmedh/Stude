from django.db import models
from users.models import StudentUser


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=50)
    body = models.TextField(max_length=5000)
    author = models.ForeignKey(StudentUser, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='blog_images')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
