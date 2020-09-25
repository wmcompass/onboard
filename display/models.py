from django.db import models


# Create your models here.

class purchase(models.Model):
    orderDate = models.DateField()
    orderNumber = models.CharField(max_length=100, blank = False, unique = True)
    username = models.CharField(max_length=250, blank = False)
    customerDesc = models.CharField(max_length=250)
    orderDesc = models.CharField(max_length=500)
    amount = models.FloatField(blank = False)
    group = models.CharField(max_length=250 , blank=False)

    def __str__ (self):
        return '%s %s %s' % (self.orderNumber, self.customerDesc, self.group)

class displayBackground(models.Model):
    image = models.ImageField(upload_to='display/images/', blank=True)

class custID(models.Model):
    username = models.CharField(max_length=250, unique=True, blank=False)
    customerDesc = models.CharField(max_length=250, blank=False)
    group = models.CharField(max_length=250 ,blank=False)
    level = models.CharField(max_length=250, blank=False)
    isAdmin = models.BooleanField(default=False)


    def __str__ (self):
        return '%s %s %s %s' % ( self.username, self.group , self.level, self.isAdmin)