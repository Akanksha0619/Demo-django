
# Create your models here.
from PIL import Image
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='def.jpg', upload_to='profile_pics')
    skills = models.TextField(default='')
    bio = models.TextField(default='')
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    batch = models.CharField(max_length=50, null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)
    enrollment_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the superclass's save() method

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




