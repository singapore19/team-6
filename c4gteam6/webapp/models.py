from django.db import models

# Create your models here.

class UserMetadata(models.Model):
    u_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    u_name = models.CharField(max_length=50, null=True)
    u_age = models.IntegerField(null=True)
    u_gender = models.CharField(max_length=6, null=True)
    u_race = models.CharField(max_length=20, null=True)
    u_availdays = models.CharField(max_length=8, null=True)
    u_availtime = models.CharField(max_length=10, null=True)

class ReportData(models.Model):
    h_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    h_agerange = models.CharField(max_length=10, null=True)
    h_gender = models.CharField(max_length=6, null=True)
    h_race = models.CharField(max_length=20, null=True)
    h_location = models.CharField(max_length=100, null=True)
    h_description = models.TextField(null=True)