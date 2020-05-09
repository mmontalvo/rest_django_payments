import uuid
from django.db import models

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deal_reference = models.CharField(max_length=128)
    currency_pair = models.CharField(max_length=8)
    buy_currency = models.CharField(max_length=4)
    sell_currency = models.CharField(max_length=4)
    amount = models.IntegerField(default=0)
    client_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)

    def __str__(self):
        return self.deal_reference

class BankTransfer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment = models.ForeignKey(Payment, null=True, on_delete=models.SET_NULL)
    bank_name = models.CharField(max_length=128)
    iban_bank_account = models.CharField(max_length=24)
    status = models.CharField(max_length=24)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.iban_bank_account