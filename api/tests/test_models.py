from django.test import TestCase
from ..models import Payment

class PaymentTest(TestCase):
    """ Test module for Payment model """

    def setUp(self):
        Payment.objects.create(
            deal_reference='MNN-DJANGO-PAY-20200503212231', currency_pair='GBPEUR', sell_currency='GBP',
            buy_currency='EUR', amount=10000, client_id='7f1f1d95-4b3e-404f-a44c-919ccafbc09d')
    def test_payment_deal_reference(self):
        payment_gbpeur = Payment.objects.get(deal_reference='MNN-DJANGO-PAY-20200503212231')
        self.assertEqual(
            payment_gbpeur.get_sell_buy_format(), "GBPEUR")
