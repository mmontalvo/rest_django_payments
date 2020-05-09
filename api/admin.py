from django.contrib import admin
from .models import Payment, BankTransfer

admin.site.register(Payment)
admin.site.register(BankTransfer)
