from django.db import models

# Create your models here.

class UserMetadata(models.Model):
    submitTime = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateField(null=True)


class ReportData(models.Model):
    submitTime = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateField(null=True)

