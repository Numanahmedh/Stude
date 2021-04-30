from django.db import models
from users.models import StudentUser


class AvailableNotes(models.Model):
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=100)
    module_number = models.CharField(max_length=100)
    notes_file = models.FileField(upload_to='notes_files')
    student_user = models.ForeignKey(StudentUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subject_code


class RequestedNotes(models.Model):
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=100)
    module_number = models.CharField(max_length=100)
    student_user = models.ForeignKey(StudentUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subject_code
