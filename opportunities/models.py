from django.db import models
from users.models import StudentUser


class Event(models.Model):
    event_category = [
        ('internships', 'Internships'),
        ('competitions', 'Competitions'),
        ('hackathons', 'Hackathons'),
        ('workshops', 'Workshops'),
    ]

    event_title = models.CharField(max_length=150)
    event_description = models.CharField(max_length=300)
    event_category = models.CharField(max_length=50, choices=event_category, default='workshops')
    event_details = models.TextField(max_length=5000)
    event_image1 = models.ImageField(upload_to='blog_images')
    event_image2 = models.ImageField(upload_to='blog_images')
    date = models.DateTimeField(auto_now_add=True)
    student_user = models.ForeignKey(StudentUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.event_title
