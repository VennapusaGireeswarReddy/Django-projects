from django.urls import path
from . import views

urlpatterns = [
    path('register',views.accountRegister,name='register'),
    path('balance',views.balanceEnquiry,name='balance'),
    path('deposit',views.deposit,name='deposit'),
    path('withdrawl',views.withdrawl,name='withdrawl'),
    path('changepin',views.changePin,name='changepin'),
    path('details',views.accountDetails,name='details'),
    path('',views.home,name='home'),
    path('transaction',views.transaction,name='transaction'),
    path('exit',views.exit,name='exit'),
]