from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


class QueryBuilderData(models.Model):
    keyword = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    year_founded = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    employee_from = models.IntegerField(blank=True, null=True)
    employee_to = models.IntegerField(blank=True, null=True)


