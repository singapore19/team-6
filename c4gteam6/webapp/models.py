from django.db import models

# Create your models here.

class UserMetadata(models.Model):
    u_timestamp = models.DateTimeField(auto_now_add=True)
    u_name = models.CharField(max_length=50)
    u_age = models.IntegerField()
    u_gender = models.CharFieldm(max_length=6)
    u_race = models.CharField(max_length=20)
    u_availdays = models.CharField(max_length=8)
    u_availtime = models.CharField(max_length=10)

class ReportData(models.Model):
    h_timestamp = models.DateTimeField(auto_now_add=True)
    h_agerange = models.CharField(max_length=10)
    h_gender = models.CharField(max_length=6)
    h_race = modesl.CharField(max_length=20)
    h_location = models.CharField(max_length=100)
    h_description = models.TextField()