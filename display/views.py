from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import purchase
from .models import displayBackground
from .forms import addPurchaseForm
from .forms import editPurchaseForm
from .forms import editAccountForm
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
    group = custID.objects.get(username=current_user).group
    level = custID.objects.get(username=current_user).level
    Admin = custID.objects.get(username=current_user).isAdmin
    isAdmin = Admin
    if isAdmin == False:
        current_custID = custID.objects.filter(username=current_user).values_list('customerID')[0]
        purchaseparts = purchase.objects.filter(customerID__in=current_custID).order_by('-orderDate')

        # Calculate
        totalcount = purchase.objects.filter(customerID__in=current_custID).count()
        totalvalue = purchase.objects.filter(customerID__in=current_custID).aggregate(Sum('amount'))['amount__sum']

        return render(request, 'display/membershipHome.html', {'purchases': purchaseparts, 'current':current_custID, 'current_users':current_user, 'isAdmin': isAdmin, 'totalcount': totalcount, 'totalvalue': totalvalue, 'level': level, 'group':group})
    else:
            if group == 'super':
                purchaseparts = purchase.objects.all()
                return render(request, 'display/membershipHome.html', {'purchases': purchaseparts, 'current_users':current_user, 'isAdmin': isAdmin, 'level': level, 'group':group})
            else:
                purchaseparts = purchase.objects.filter(group=group)
                return render(request, 'display/membershipHome.html', {'purchases': purchaseparts, 'current_users':current_user, 'isAdmin': isAdmin, 'level': level, 'group':group})



@login_required
def addPurchase(request):
    current_user = User.objects.get(username=request.user.username)
    Admin = custID.objects.get(username=current_user).isAdmin
    isAdmin = Admin
    if isAdmin:
        if request.method == "GET":
            current_user = User.objects.get(username=request.user.username)
            group = custID.objects.get(username=current_user).group
            return render(request, 'display/addPurchase.html', {'form' : addPurchaseForm , 'group':group , 'isAdmin': isAdmin})
        else:
            try:
                form = addPurchaseForm(request.POST)
                form.save()
                return redirect('membershipHome')
            except ValueError:
                return render(request, 'display/addPurchase.html', {'form': addPurchaseForm, 'error':'Bad data type'})
    else:
        return render(request, 'verify/home.html')


@login_required
def editPurchase(request, purchase_pk):
    current_user = User.objects.get(username=request.user.username)
    group = custID.objects.get(username=current_user).group
    Admin = custID.objects.get(username=current_user).isAdmin
    isAdmin = Admin
    if isAdmin:
        if group != 'super':
            editpurchase = get_object_or_404(purchase, pk= purchase_pk,group=group)
            if request.method == "GET":
                form = editPurchaseForm(instance=editpurchase)
                return render(request, 'display/editPurchase.html', {'purchase': editpurchase,'form': form , 'isAdmin': isAdmin})
            else:
                try:
                    form = editPurchaseForm(request.POST, instance=editpurchase)
                    form.save()
                    return redirect('membershipHome')
                except ValueError:
                    return render(request, 'display/editPurchase.html', {'purchase': editpurchase}, {'form':form}, {'error':'Bad data type'})
        else:
            editpurchase = get_object_or_404(purchase, pk=purchase_pk)
            if request.method == "GET":
                form = editPurchaseForm(instance=editpurchase)
                return render(request, 'display/editPurchase.html', {'purchase': editpurchase, 'form': form , 'isAdmin': isAdmin})
            else:
                try:
                    form = editPurchaseForm(request.POST, instance=editpurchase)
                    form.save()
                    return redirect('membershipHome')
                except ValueError:
                    return render(request, 'display/editPurchase.html', {'purchase': editpurchase}, {'form': form},
                                  {'error': 'Bad data type'})
    else:
        return render(request, 'verify/home.html')


@login_required
def deletePurchase(request, purchase_pk):
    current_user = User.objects.get(username=request.user.username)
    Admin = custID.objects.get(username=current_user).isAdmin
    isAdmin = Admin
    if isAdmin:
        deletepurchase = get_object_or_404(purchase, pk= purchase_pk)
        if request.method == "POST":
            deletepurchase.delete()
            return redirect('membershipHome')
    else:
        return render(request, 'verify/home.html')


@login_required
def manageAccount(request):
    current_user = User.objects.get(username=request.user.username)
    group = custID.objects.get(username=current_user).group
    Admin = custID.objects.get(username=current_user).isAdmin
    isAdmin = Admin
    if isAdmin:
        if group != 'super':
            accounts = custID.objects.filter(group=group)
            return render(request, 'display/manageAccount.html', {'accounts': accounts, 'group': group, 'isAdmin': isAdmin})
        else:
            accounts = custID.objects.all()
            return render(request, 'display/manageAccount.html', {'accounts': accounts, 'group': group, 'isAdmin': isAdmin})
    else:
        return render(request, 'verify/home.html')

@login_required
def editAccount(request, custID_pk):
    current_user = User.objects.get(username=request.user.username)
    group = custID.objects.get(username=current_user).group
    Admin = custID.objects.get(username=current_user).isAdmin
    isAdmin = Admin
    if isAdmin:
        if group != 'super':
            editAccount = get_object_or_404(custID, pk= custID_pk, group=group)
            if request.method == "GET":
                form = editAccountForm(instance=editAccount)
                return render(request, 'display/editAccount.html', {'form': form , 'isAdmin': isAdmin})
            else:
                try:
                    form = editAccountForm(request.POST, instance=editAccount)
                    form.save()
                    return redirect('membershipHome')
                except ValueError:
                    return render(request, 'display/editAccount.html',  {'editaccount': editAccount, 'form':form, 'error':'Bad data type'})
        else:
            editAccount = get_object_or_404(custID, pk=custID_pk)
            if request.method == "GET":
                form = editAccountForm(instance=editAccount)
                return render(request, 'display/editAccount.html', {'form': form , 'isAdmin': isAdmin})
            else:
                try:
                    form = editAccountForm(request.POST, instance=editAccount)
                    form.save()
                    return redirect('membershipHome')
                except ValueError:
                    return render(request, 'display/editAccount.html',
                                  {'editaccount': editAccount, 'form': form, 'error': 'Bad data type'})


    else:
        return render(request, 'verify/home.html')