
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
        fields = ['customerID', 'username', 'customerDesc', 'group', 'isAdmin']

class addPurchaseForm(ModelForm):
    class Meta:
        model = purchase
        fields = ['orderDate', 'orderNumber', 'customerID', 'customerDesc', 'pressDesc',
                  'currency', 'amount', 'NTamount', 'country', 'group']

class editPurchaseForm(ModelForm):
    class Meta:
        model = purchase
        fields = ['orderDate', 'orderNumber', 'customerID', 'customerDesc', 'pressDesc',
                  'currency', 'amount', 'NTamount', 'country']