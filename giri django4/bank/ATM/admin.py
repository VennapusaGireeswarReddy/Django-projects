from django.contrib import admin
from . models import Transaction,Account
# Register your models here.
admin.site.register(Account),
admin.site.register(Transaction)
