from rest_framework import viewsets

from .serializers import PaymentSerializer, BankTransferSerializer
from .models import Payment, BankTransfer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class BankTransferViewSet(viewsets.ModelViewSet):
    queryset = BankTransfer.objects.all()
    serializer_class = BankTransferSerializer