from django.forms import ValidationError
from django.test import TestCase
from datetime import datetime
from ong.models import Ong
from payment.models import Payment
from project.models import Project


class PaymentTestCase(TestCase):
    def setUp(self):
        self.ong = Ong.objects.create(name="VidesSur")
        self.project = Project.objects.create(title="projecto", country="Spain", start_date=datetime(2023, 3, 11), end_date=datetime(
            2024, 11, 28), number_of_beneficiaries=2, amount=7, announcement_date=datetime(2022, 11, 28), ong=Ong.objects.get(name="VidesSur"))
        Payment.objects.create(concept="concept", payday=datetime(
            2023, 3, 11), amount=10, ong=self.ong, paid=True)
        Payment.objects.create(concept="concept", payday=datetime(
            2022, 11, 28), amount=105.56, ong=self.ong, paid=True)
        Payment.objects.create(concept="concept", payday=datetime(
            2010, 6, 9), amount=1000.1, ong=self.ong, paid=False, project=self.project)

    def test_payment_creation(self):
        payment = Payment.objects.get(amount=10)
        self.assertEqual(payment.concept, "concept")
        self.assertEqual(float(payment.amount), 10.)
        self.assertEqual(payment.payday.strftime('%d/%m/%Y'),
                         datetime(2023, 3, 11).strftime('%d/%m/%Y'))
        self.assertEqual(payment.paid, True)
        self.assertEqual(payment.ong, self.ong)

        payment2 = Payment.objects.get(amount=105.56)
        self.assertEqual(payment2.concept, "concept")
        self.assertEqual(float(payment2.amount), 105.56)
        self.assertEqual(payment2.payday.strftime('%d/%m/%Y'),
                         datetime(2022, 11, 28).strftime('%d/%m/%Y'))
        self.assertEqual(payment2.paid, True)
        self.assertEqual(payment2.ong, self.ong)

        payment3 = Payment.objects.get(amount=1000.1)
        self.assertEqual(payment3.concept, "concept")
        self.assertEqual(float(payment3.amount), 1000.1)
        self.assertEqual(payment3.payday.strftime('%d/%m/%Y'),
                         datetime(2010, 6, 9).strftime('%d/%m/%Y'))
        self.assertEqual(payment3.paid, False)
        self.assertEqual(payment3.ong, self.ong)
        self.assertEqual(payment3.project.title, "projecto")

    def test_payment_update(self):
        payment = Payment.objects.get(amount=105.56)
        payment.amount = 1009.3
        payment.payday = datetime(2001, 3, 12)
        payment.paid = False
        payment.save()
        self.assertEqual(float(payment.amount), 1009.3)
        self.assertEqual(payment.payday.strftime('%d/%m/%Y'),
                         datetime(2001, 3, 12).strftime('%d/%m/%Y'))
        self.assertEqual(payment.paid, False)

    def test_payment_delete(self):
        payment = Payment.objects.get(amount=1000.1)
        payment.delete()
        self.assertEqual(Payment.objects.count(), 2)

    def test_payment_create_negative_amount(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(payday=datetime(
                2020, 2, 31), amount=-1, ong=self.ong)

    def test_payment_create_null_ong(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(payday=datetime(2020, 2, 31), amount=-1)

    def test_payment_create_null_concept(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(
                concept=None, payday=datetime(2020, 2, 31), amount=-1)

    def test_payment_create_blank_concept(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(
                concept="", payday=datetime(2020, 2, 31), amount=-1)

    def test_payment_create_max_length_concept(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(
                concept="C"*151, payday=datetime(2020, 2, 31), amount=-1)

    def test_payment_create_max_digits_amount(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(payday=datetime(
                2020, 2, 31), amount=10000000000, ong=self.ong)

    def test_payment_create_amount_not_decimal(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(payday=datetime(
                2020, 2, 31), amount="1.111", ong=self.ong)

    def test_payment_create_payday_not_datetime(self):
        with self.assertRaises(ValidationError):
            Payment.objects.create(payday="2020-02-31",
                                   amount=1.11, ong=self.ong)

    def test_payment_create_paid_not_boolean(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(payday=datetime(
                2020, 2, 31), amount=1.11, paid="True", ong=self.ong)

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

    def test_payment_update_null_concept(self):
        payment = Payment.objects.get(amount=105.56)
        with self.assertRaises(Exception):
            payment.concept = None
            payment.save()

    def test_payment_update_blank_concept(self):
        payment = Payment.objects.get(amount=105.56)
        with self.assertRaises(Exception):
            payment.concept = ""
            payment.full_clean()
            payment.save()

    def test_payment_update_max_length_concept(self):
        payment = Payment.objects.get(amount=105.56)
        with self.assertRaises(Exception):
            payment.concept = "C"*151
            payment.save()
