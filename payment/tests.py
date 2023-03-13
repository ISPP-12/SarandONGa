from django.test import TestCase
from datetime import datetime
from payment.models import Payment

class PaymentTestCase(TestCase):
    def setUp(self):
        Payment.objects.create(payday=datetime(2023,3,11), amount=10)
        Payment.objects.create(payday=datetime(2022,11,28), amount=105.56)
        Payment.objects.create(payday=datetime(2010,6,9), amount=1000.1)

    def test_payment_creation(self):
        payment = Payment.objects.get(amount=10)
        self.assertEqual(float(payment.amount), 10.)
        self.assertEqual(payment.payday.strftime('%d/%m/%Y'), datetime(2023,3,11).strftime('%d/%m/%Y'))

        payment2 = Payment.objects.get(amount=105.56)
        self.assertEqual(float(payment2.amount), 105.56)
        self.assertEqual(payment2.payday.strftime('%d/%m/%Y'), datetime(2022,11,28).strftime('%d/%m/%Y'))

        payment3 = Payment.objects.get(amount=1000.1)
        self.assertEqual(float(payment3.amount), 1000.1)
        self.assertEqual(payment3.payday.strftime('%d/%m/%Y'), datetime(2010,6,9).strftime('%d/%m/%Y'))

    def test_payment_update(self):
        payment = Payment.objects.get(amount=105.56)
        payment.amount = 1009.3
        payment.payday= datetime(2001,3,12)
        payment.save()
        self.assertEqual(float(payment.amount), 1009.3)
        self.assertEqual(payment.payday.strftime('%d/%m/%Y'), datetime(2001,3,12).strftime('%d/%m/%Y'))

    def test_payment_delete(self):
        payment = Payment.objects.get(amount=1000.1)
        payment.delete()
        self.assertEqual(Payment.objects.count(), 2)

    def  test_payment_negative_payday(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(payday=datetime(2020,2,31), amount=-1)

