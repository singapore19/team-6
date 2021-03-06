# Generated by Django 2.2.6 on 2019-10-04 05:35

from django.db import migrations, models
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20191004_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewReportData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('h_location', models.CharField(max_length=100, null=True)),
                ('h_image', models.ImageField(blank=True, max_length=254, null=True, upload_to=webapp.models.productFile)),
                ('h_gender', models.CharField(max_length=6, null=True)),
                ('h_race', models.CharField(max_length=20, null=True)),
                ('h_frequency', models.CharField(max_length=20, null=True)),
                ('h_agerange', models.CharField(max_length=10, null=True)),
                ('h_risk', models.CharField(max_length=10, null=True)),
                ('h_description', models.TextField(null=True)),
            ],
        ),
    ]
