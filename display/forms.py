
from django.forms import ModelForm
from .models import purchase
from .models import custID

class editAccountForm(ModelForm):
    class Meta:
        model = custID
        fields = ['customerDesc','level' , 'isAdmin']

class custIDForm(ModelForm):
    class Meta:
        model = custID
        fields = ['username', 'customerDesc', 'group', 'isAdmin', 'level']

class addPurchaseForm(ModelForm):
    class Meta:
        model = purchase
        fields = ['orderDate', 'orderNumber', 'username', 'customerDesc', 'orderDesc', 'amount', 'group']

class editPurchaseForm(ModelForm):
    class Meta:
        model = purchase
        fields = ['orderDate', 'orderNumber', 'username', 'customerDesc', 'orderDesc', 'amount']