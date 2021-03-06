# Generated by Django 2.2.6 on 2019-10-04 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191004_0259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportdata',
            old_name='submitTime',
            new_name='h_timestamp',
        ),
        migrations.RenameField(
            model_name='usermetadata',
            old_name='submitTime',
            new_name='u_timestamp',
        ),
        migrations.RemoveField(
            model_name='reportdata',
            name='date',
        ),
        migrations.RemoveField(
            model_name='usermetadata',
            name='date',
        ),
        migrations.AddField(
            model_name='reportdata',
            name='h_agerange',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='reportdata',
            name='h_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='reportdata',
            name='h_gender',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='reportdata',
            name='h_location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='reportdata',
            name='h_race',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermetadata',
            name='u_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usermetadata',
            name='u_availdays',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='usermetadata',
            name='u_availtime',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='usermetadata',
            name='u_gender',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='usermetadata',
            name='u_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usermetadata',
            name='u_race',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
