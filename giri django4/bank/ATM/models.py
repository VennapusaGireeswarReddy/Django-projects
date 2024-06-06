from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    name = models.CharField( max_length=50)
    accountNo = models.BigIntegerField()
    bankName = models.TextField()
    IFSCcode = models.TextField()
    cardNumber = models.BigIntegerField()
    cvv = models.IntegerField()
    pin = models.IntegerField()
    expDate = models.DateField(auto_now=False, auto_now_add=False)
    fixedAmount = models.IntegerField(default=0)
    balance = models.DecimalField( max_digits=10, decimal_places=2)
   

class Transaction(models.Model):
    balance = models.DecimalField( max_digits=10, decimal_places=2)
    withdrawlAmount = models.BigIntegerField(default=0)
    depoistedAmount = models.BigIntegerField(default=0)
    uid=models.ForeignKey(Account, on_delete=models.CASCADE)

def __str__(self):
    return self.name

