from django.db import models
from django.contrib.auth.models import AbstractUser


class StudentUser(AbstractUser):
    fullname = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    year_sem = models.CharField(max_length=50)
    college_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
