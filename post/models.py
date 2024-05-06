from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Job(models.Model):
    COMPANY_LOGO = 'default_logo.png'

    company_name = models.CharField(max_length=100)
    company_image = models.ImageField(blank=True, null=True)
    position = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateField()
    date_posted = models.DateTimeField(default=timezone.now)
    required_skills = models.TextField()
    location = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return f"{self.position} at {self.company_name}"


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.company_image:
            img = Image.open(self.company_image.path)

            # Define your maximum image size here
            max_width = 1000
            max_height = 600

            if img.width > max_width or img.height > max_height:
                output_size = (max_width, max_height)
                img.thumbnail(output_size)
                img.save(self.company_image.path)


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=20)
    message = models.TextField()

    def _str_(self):
        return self.name + ' - ' + self.enrollment_no


from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=20)
    branch = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
