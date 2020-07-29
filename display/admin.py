from django.contrib import admin
from .models import purchase
from .models import displayBackground
from .models import custID

# Register your models here.

admin.site.register(purchase)
admin.site.register(displayBackground)
admin.site.register(custID)


