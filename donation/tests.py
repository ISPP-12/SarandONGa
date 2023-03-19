from django.test import TestCase
from donation.models import Donation
import datetime
from ong.models import Ong


class DonationTestCase(TestCase):

    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        Donation.objects.create(
            title="donation",
            description="donation",
            created_date=datetime.date.today(),
            amount=50,
            donor_name="Jaime",
            donor_surname="Moscoso",
            donor_dni="12345678A",
            donor_address="Sevilla",
            donor_email="email@email.com",
            ong=self.ong
        )

    def test_donation_create(self):
        donation = Donation.objects.get(title="donation")
        self.assertEqual(donation.title, "donation")

    def test_donation_update(self):
        donation = Donation.objects.get(title="donation")
        donation.title = "change"
        donation.description = "change"
        donation.created_date = datetime.date(2023, 3, 4)
        donation.amount = 12
        donation.donor_name = "change"
        donation.donor_surname = "change"
        donation.donor_dni = "66666666A"
        donation.donor_address = "change"
        donation.donor_email = "change@email.com"
        self.assertEqual(donation.title, "change")
        self.assertEqual(donation.description, "change")
        self.assertEqual(donation.created_date, datetime.date(2023, 3, 4))
        self.assertEqual(donation.amount, 12)
        self.assertEqual(donation.donor_name, "change")
        self.assertEqual(donation.donor_surname, "change")
        self.assertEqual(donation.donor_dni, "66666666A")
        self.assertEqual(donation.donor_address, "change")
        self.assertEqual(donation.donor_email, "change@email.com")

    def test_donation_delete(self):
        donation = Donation.objects.get(title="donation")
        self.assertEqual(Donation.objects.count(), 1)
        donation.delete()
        self.assertEqual(Donation.objects.count(), 0)

    def test_donation_create_incorrect_title_max(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
                + "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
                description="donation",
                created_date=datetime.date.today(),
                amount=50,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_creation_date(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date="INCORRECTO",
                amount=50,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_max_digits_amount(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=12345678901,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_min_amount(self):
        with self.assertRaises(Exception):
            donation = Donation(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=0.01,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )
            donation.full_clean()
            donation.save()

    def test_donation_create_incorrect_string_amount(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount="Hola",
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_max_length_donor_name(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=50,
                donor_name="iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_max_length_donor_surname(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=50,
                donor_name="Jaime",
                donor_surname="iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
                "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
                "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_size_dni(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=10,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="123456789A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_max_length_address(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=10,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
                "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
                "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_email(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=10,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="123456789A",
                donor_address="Sevilla",
                donor_email="email",
                ong=self.ong
            )

    def test_donation_update_incorrect_title_max(self):
        donation = Donation.objects.get(title="donation")
        donation.title = "donation"*50
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_title_max(self):
        donation = Donation.objects.get(title="donation")
        donation.title = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_blank_title_max(self):
        donation = Donation.objects.get(title="donation")
        donation.title = ""
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_creation_date(self):
        donation = Donation.objects.get(title="donation")
        donation.created_date = "bad_date"
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_creation_date(self):
        donation = Donation.objects.get(title="donation")
        donation.created_date = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_max_digits_amount(self):
        donation = Donation.objects.get(title="donation")
        donation.amount = 10000000000
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_amount(self):
        donation = Donation.objects.get(title="donation")
        donation.amount = "bad_amount"
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_max_digits_amount(self):
        donation = Donation.objects.get(title="donation")
        donation.amount = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_min_amount(self):
        donation = Donation.objects.get(title="donation")
        donation.amount = -1
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_max_length_donor_name(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_name = "Pedro"*50
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_blank_donor_name(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_name = ""
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_donor_name(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_name = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_max_length_donor_surname(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_surname = "Pedro"*250
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_blank_donor_surname(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_surname = ""
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_donor_surname(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_surname = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_size_dni(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_dni = "26"*7
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_size_dni(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_dni = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_blank_size_dni(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_dni = ""
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_size_address(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_address = "Address"*200
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_size_address(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_address = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_blank_size_address(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_address = ""
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_email(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_email = "email"
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_email(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_email = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_blank_email(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_email = ""
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()
