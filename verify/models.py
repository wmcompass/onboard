from django.db import models


class verifyBackground(models.Model):
    image = models.ImageField(upload_to='verify/images/', blank=True)
# Create your models here.
