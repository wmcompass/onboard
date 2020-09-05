from django.db import models


# Create your models here.

class purchase(models.Model):
    orderDate = models.DateField()
    orderNumber = models.CharField(max_length=100)
    username = models.CharField(max_length=250, blank = True)
    customerDesc = models.CharField(max_length=250)
    orderDesc = models.CharField(max_length=500, blank=True)
    amount = models.FloatField()
    group = models.CharField(max_length=250)

    def __str__ (self):
        return '%s %s %s' % (self.orderNumber, self.customerDesc, self.group)

class displayBackground(models.Model):
    image = models.ImageField(upload_to='display/images/', blank=True)

class custID(models.Model):
    username = models.CharField(max_length=250)
    customerDesc = models.CharField(max_length=250)
    group = models.CharField(max_length=250)
    level = models.CharField(max_length=250)
    isAdmin = models.BooleanField(default=False)


    def __str__ (self):
        return '%s %s %s %s' % ( self.username, self.group , self.level, self.isAdmin)