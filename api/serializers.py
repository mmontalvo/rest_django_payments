from rest_framework import serializers

from .models import Payment
from .models import BankTransfer

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = (
          'id', 'deal_reference', 'currency_pair', 'buy_currency', 'sell_currency',
          'amount', 'client_id'
        )

class BankTransferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankTransfer
        fields = ('id', 'payment', 'bank_name', 'iban_bank_account', 'status', 'amount')