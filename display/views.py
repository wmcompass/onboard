from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import purchase
from .models import displayBackground
from .forms import managePurchaseForm
from .forms import addPurchaseForm
from .models import custID

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# To include python calculation packages
from django.db.models import Sum

from verify import views

@login_required
def membershipHome(request):
    current_user = User.objects.get(username=request.user.username)
    Admin = custID.objects.get(username=current_user).isAdmin
    isAdmin = Admin
    if isAdmin == False:
        current_custID = custID.objects.filter(username=current_user).values_list('customerID')[0]
        purchaseparts = purchase.objects.filter(customerID__in=current_custID).order_by('-orderDate')

        # Calculate
        totalcount = purchase.objects.filter(customerID__in=current_custID).count()
        totalvalue = purchase.objects.filter(customerID__in=current_custID).aggregate(Sum('amount'))['amount__sum']

        return render(request, 'display/membershipHome.html', {'purchases': purchaseparts, 'current':current_custID, 'current_users':current_user, 'isAdmin': isAdmin, 'totalcount': totalcount, 'totalvalue': totalvalue})
    else:
        purchaseparts = purchase.objects.all()
        return render(request, 'display/membershipHome.html', {'purchases': purchaseparts, 'current_users':current_user, 'isAdmin': isAdmin})
        #return render(request, 'display/base.html', {'admin': Admin})


@login_required
def addPurchase(request):
    if request.method == "GET":
        return render(request, 'display/addPurchase.html', {'form' : addPurchaseForm })
    else:
        try:
            form = addPurchaseForm(request.POST)
            form.save()
            return redirect('membershipHome')
        except ValueError:
            return render(request, 'display/addPurchase.html', {'form': addPurchaseForm, 'error':'Bad data type'})

@login_required
def editPurchase(request, purchase_pk):
    editpurchase = get_object_or_404(purchase, pk= purchase_pk)
    if request.method == "GET":
        form = addPurchaseForm(instance=editpurchase)
        return render(request, 'display/editPurchase.html', {'purchase': editpurchase,'form': form})
    else:
        try:
            form = addPurchaseForm(request.POST, instance=editpurchase)
            form.save()
            return redirect('membershipHome')
        except ValueError:
            return render(request, 'display/editPurchase.html', {'purchase': editpurchase}, {'form':form}, {'error':'Bad data type'})

@login_required
def deletePurchase(request, purchase_pk):
    deletepurchase = get_object_or_404(purchase, pk= purchase_pk)
    if request.method == "POST":
        deletepurchase.delete()
        return redirect('membershipHome')


@login_required
def managePurchase(request):
    if request.method == "GET":
        background = displayBackground.objects.all()
        return render(request, 'display/managePurchase.html', {'backgrounds': background, 'form': managePurchaseForm()})
    else:
        try:
            form = managePurchaseForm(request.POST)
            form.save()
            # newManagePurchase = form.save(commit=False)
            #newManagePurchase.user = request.user
            #newManagePurchase.save()
            background = displayBackground.objects.all()
            return render(request, 'display/managePurchase.html', {'backgrounds': background, 'form': managePurchaseForm()})
        except ValueError:
            background = displayBackground.objects.all()
            return render(request, 'display/managePurchase.html', {'backgrounds': background, 'form': managePurchaseForm(), 'error': '資料型態有錯誤'})


