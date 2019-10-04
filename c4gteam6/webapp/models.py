from django.db import models

# Create your models here.
def productFile(instance, filename):
    return '/'.join( ['products', str(instance.id), filename] )

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

class NewReportData(models.Model):
    h_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    h_latitude = models.CharField(max_length=100, null=True)
    h_longitude = models.CharField(max_length=100, null=True)
    image = models.ImageField(
            upload_to=productFile,
            max_length=254, blank=True, null=True
        )
    h_gender = models.CharField(max_length=6, null=True)
    h_race = models.CharField(max_length=20, null=True)
    h_frequency = models.CharField(max_length=20, null=True)
    h_agerange = models.CharField(max_length=10, null=True)
    h_risk = models.CharField(max_length=10, null=True)
    h_description = models.TextField(null=True)