from django.forms import ValidationError
from django.test import TestCase
from datetime import datetime
from ong.models import Ong
from payment.models import Payment
from proyect.models import Proyect

class PaymentTestCase(TestCase):
    def setUp(self):
        Ong.objects.create(name="VidesSur")
        Proyect.objects.create(title="Proyecto", country="Spain", start_date = datetime(2023,3,11), end_date= datetime(2024,11,28), number_of_beneficiaries=2, amount=7, announcement_date=datetime(2022,11,28), ong=Ong.objects.get(name="VidesSur"))
        proyect = Proyect.objects.get(title="Proyecto")
        Payment.objects.create(payday=datetime(2023,3,11), amount=10, paid=True)
        Payment.objects.create(payday=datetime(2022,11,28), amount=105.56, paid=True)
        Payment.objects.create(payday=datetime(2010,6,9), amount=1000.1, paid=False, proyect=proyect)

    def test_payment_creation(self):
        payment = Payment.objects.get(amount=10)
        self.assertEqual(float(payment.amount), 10.)
        self.assertEqual(payment.payday.strftime('%d/%m/%Y'), datetime(2023,3,11).strftime('%d/%m/%Y'))
        self.assertEqual(payment.paid, True)

        payment2 = Payment.objects.get(amount=105.56)
        self.assertEqual(float(payment2.amount), 105.56)
        self.assertEqual(payment2.payday.strftime('%d/%m/%Y'), datetime(2022,11,28).strftime('%d/%m/%Y'))
        self.assertEqual(payment2.paid, True)

        payment3 = Payment.objects.get(amount=1000.1)
        self.assertEqual(float(payment3.amount), 1000.1)
        self.assertEqual(payment3.payday.strftime('%d/%m/%Y'), datetime(2010,6,9).strftime('%d/%m/%Y'))
        self.assertEqual(payment3.paid, False)
        self.assertEqual(payment3.proyect.title, "Proyecto")

    def test_payment_update(self):
        payment = Payment.objects.get(amount=105.56)
        payment.amount = 1009.3
        payment.payday= datetime(2001,3,12)
        payment.paid = False
        payment.save()
        self.assertEqual(float(payment.amount), 1009.3)
        self.assertEqual(payment.payday.strftime('%d/%m/%Y'), datetime(2001,3,12).strftime('%d/%m/%Y'))
        self.assertEqual(payment.paid, False)

    def test_payment_delete(self):
        payment = Payment.objects.get(amount=1000.1)
        payment.delete()
        self.assertEqual(Payment.objects.count(), 2)

    def  test_payment_create_negative_amount(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(payday=datetime(2020,2,31), amount=-1)

    def test_payment_create_max_digits_amount(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(payday=datetime(2020,2,31), amount=10000000000)

    def test_payment_create_amount_not_decimal(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(payday=datetime(2020,2,31), amount="1.111")
    
    def test_payment_create_payday_not_datetime(self):
        with self.assertRaises(ValidationError):
            Payment.objects.create(payday="2020-02-31", amount=1.11)

    def test_payment_create_paid_not_boolean(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(payday=datetime(2020,2,31), amount=1.11, paid="True")

    def test_payment_update_negative_amount(self):
        payment = Payment.objects.get(amount=105.56)
        with self.assertRaises(Exception):
            payment.amount = -1
            payment.save()

    def test_payment_update_max_digits_amount(self):
        payment = Payment.objects.get(amount=105.56)
        with self.assertRaises(Exception):
            payment.amount = 10000000000
            payment.save()

    def test_payment_update_amount_not_decimal(self):
        payment = Payment.objects.get(amount=105.56)
        with self.assertRaises(Exception):
            payment.amount = "1.78"
            payment.save()
    
    def test_payment_update_payday_not_datetime(self):
        payment = Payment.objects.get(amount=105.56)
        with self.assertRaises(Exception):
            payment.payday = "2020-02-31"
            payment.save()
    
    def test_payment_update_paid_not_boolean(self):
        payment = Payment.objects.get(amount=105.56)
        with self.assertRaises(Exception):
            payment.paid = "True"
            payment.save()
    



