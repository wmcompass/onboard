from django.db import models


# Create your models here.

class purchase(models.Model):
    orderDate = models.DateField()
    orderNumber = models.CharField(max_length=100)
    customerID = models.CharField(max_length=100)
    customerDesc = models.CharField(max_length=250)
    pressDesc = models.CharField(max_length=250)
    currency = models.CharField(max_length=20)
    amount = models.FloatField()
    NTamount = models.FloatField()
    country = models.CharField(max_length=100)
    group = models.CharField(max_length=250)

    def __str__ (self):
        return '%s %s %s' % (self.orderNumber, self.customerDesc, self.customerID)

class displayBackground(models.Model):
    image = models.ImageField(upload_to='display/images/', blank=True)

class custID(models.Model):
    customerID = models.CharField(max_length=100)
    username = models.CharField(max_length=250)
    customerDesc = models.CharField(max_length=250)
    group = models.CharField(max_length=250)
    isAdmin = models.BooleanField(default=False)

    def __str__ (self):
        return '%s %s %s %s' % (self.customerID, self.username, self.group , self.isAdmin)

