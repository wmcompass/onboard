"""membership URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from verify import views as vv
from display import views as dv

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),

    #會員註冊頁面
    path('signup', vv.signup, name='signup'),

    #管理者註冊
    path('adminRegister', vv.adminRegister , name='adminRegister'),

    #登入後會員頁面
    path('membershipHome/', dv.membershipHome, name='membershipHome'),

    #會員登入頁面 / 首頁
    path('', vv.home, name='home'),

    #會員登出頁面
    path('logout', vv.logoutuser, name='logoutuser'),

    #管理使用者帳號 - TBD
    path('manageAccount', dv.manageAccount, name='manageAccount'),

    #增加交易資料
    path('addPurchase', dv.addPurchase, name='addPurchase'),

    #修改交易資料
    path('purchase/<int:purchase_pk>', dv.editPurchase, name='editPurchase'),

    # 刪除交易資料
    path('purchase/<int:purchase_pk>/delete', dv.deletePurchase, name='deletePurchase'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

