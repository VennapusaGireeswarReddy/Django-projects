from decimal import Decimal, InvalidOperation
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as login_user,logout
from django.contrib import messages
from .models import Account,Transaction
from django.db.models import Q

# Create your views here.
def balanceEnquiry(request):
    if request.method == "POST":
        cardNumber=request.POST.get('cardNumber')
        pin=request.POST.get('pin')
        account=Account.objects.filter(cardNumber=cardNumber,pin=pin)
        if account is not None:
           return render(request,'balance.html',{'account':account})
        else:
            messages.info(request,"cardnumber or pin not matched")
            return redirect('balance')
    return render(request,'balance.html')

def withdrawl(request):
    if request.method == "POST":
        cardNumber=request.POST.get('cardNumber')
        pin=request.POST.get('pin')
        amount=request.POST.get('amount')
        try:
            amount = Decimal(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive")
        except (ValueError, InvalidOperation):
            messages.error(request, "Invalid amount entered.")
            return redirect('deposit')
        user=Account.objects.get(cardNumber=cardNumber,pin=pin)
        if user is not None:
            account=Account.objects.get(cardNumber=cardNumber)
            if amount <= account.balance-account.fixedAmount:
                messages.info(request,"please collect your amount")
                balance=account.balance-amount
                account=Account.objects.filter(cardNumber=cardNumber).update(balance=balance)
                accounttr=Transaction.objects.create(withdrawlAmount=amount,balance=balance,uid_id=user.id)
                return render(request,'withdrawl.html',{'balance':balance,'amount':amount})
                # return render(request,'withdrawl.html',{'balance'})
            else:
                messages.info(request,"insufficient balance")
                return redirect('withdrawl')
        else:
            messages.info(request,"cardnumber or pin not matched")
            return redirect('withdrawl')
    return render(request,'withdrawl.html')

         




def accountRegister(request):
    if request.method == "POST":
        name= request.POST.get('name')
        accountNo = request.POST.get('accountNo')
        email = request.POST.get('email')
        bankName =  request.POST.get('bankName')
        IFSCcode =  request.POST.get('IFSCcode')
        cardNumber =  request.POST.get('cardNumber')
        cvv = request.POST.get('cvv')
        pin = request.POST.get('pin')
        confirm_pin = request.POST.get('confirmPin')
        expDate = request.POST.get('expDate')
        fixedAmount= request.POST.get('fixedAmount')
        balance = request.POST.get('balance')
        if pin==confirm_pin:
            user=Account.objects.create(name=name,pin=pin,bankName=bankName,IFSCcode=IFSCcode,cardNumber=cardNumber,
                                          cvv=cvv,expDate=expDate,fixedAmount=fixedAmount,accountNo=accountNo,balance=balance)
            messages.info(request,'successfully registered')
            return redirect('home')
        else:
            messages.info(request,"pin number does not match")
            return redirect('register')
    return render(request,'account.html')

def deposit(request):
    if request.method == "POST":
        cardNumber=request.POST.get('cardNumber')
        pin=request.POST.get('pin')
        amount=request.POST.get('amount')
        try:
            amount = Decimal(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive")
        except (ValueError, InvalidOperation):
            messages.error(request, "Invalid amount entered.")
            return redirect('deposit')
        user=Account.objects.get(cardNumber=cardNumber,pin=pin)
        print(user)
        if user is not None:
            account=Account.objects.get(cardNumber=cardNumber,pin=pin)
            print(account.balance)
            balance = account.balance+amount
            account=Account.objects.filter(cardNumber=cardNumber).update(balance=balance)
            accounttr=Transaction.objects.create(depoistedAmount=amount,balance=balance,uid_id=user.id)
            messages.info(request,"amount is successfully deposited")
            uBalance = Decimal(balance)
            return render(request,'deposit.html',{'balance':uBalance,'amount':amount})
        else:
            messages.info(request,"cardnumber or pin not matched")
            return redirect('deposit')
    return render(request,'deposit.html')

def accountDetails(request):
    if request.method == "POST":
        cardNumber=request.POST.get('cardNumber')
        pin=request.POST.get('pin')
        user=Account.objects.get(cardNumber=cardNumber,pin=pin)
        if user is not None:
            account=Account.objects.filter(cardNumber=cardNumber,pin=pin)
            return render(request,'accountDetails.html',{'account':account})
        else:
            messages.info(request,"cardnumber or pin not matched")
            return redirect('details')
    return render(request,"accountDetails.html")

def changePin(request):
    if request.method == "POST":
        cardNumber=request.POST.get('cardNumber')
        pin=request.POST.get('pin')
        accountNo=request.POST.get('accountNo')
        yourPin = request.POST.get('yourPin')
        user=Account.objects.get(cardNumber=cardNumber,pin=pin,accountNo=accountNo)
        if user is not None:
            Account.objects.filter(cardNumber=cardNumber).update(pin=yourPin)
            messages.info(request,"your pin no is successfully changed")
            return redirect('changepin')
        else:
            messages.info(request,"cardnumber or pin not matched")
            return redirect('changepin')
    return render(request,"pin.html")

def home(request):
    return render(request,'home.html')

def exit(request):
    messages.info(request,"Thank you please visit again")
    return redirect('home')

def transaction(request):
    if request.method == "POST":
        cardNumber=request.POST.get('cardNumber')
        pin=request.POST.get('pin')
        user=Account.objects.get(cardNumber=cardNumber,pin=pin)
        if user is not None:
            transaction = Transaction.objects.filter(uid_id=user.id)
            print(transaction)
            messages.info(request,"Here your Transaction Details")
            return render(request,'transaction.html',{'transactions':transaction,'user':user})
        else:
            messages.info(request,"cardnumber or pin not matched")
            return redirect("transaction")
    return render(request,'ministatement.html')
        



# def authenticate(self, request, cardNumber=None, pin=None):
#         try:
#             account = Account.objects.get(cardNumber=cardNumber, pin=pin)
#             return account.user  # Assuming 'user' is a ForeignKey to User in Account model
#         except Account.DoesNotExist:
#             return None

    
    




# def signout(request):
#     logout(request)
#     messages.info(request,"you are successfully logged out")
#     return redirect('home')

