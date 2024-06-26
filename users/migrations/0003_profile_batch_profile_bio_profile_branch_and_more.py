# Generated by Django 5.0.2 on 2024-03-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='batch',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='branch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='enrollment_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes'),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.TextField(default=''),
        ),
    ]
