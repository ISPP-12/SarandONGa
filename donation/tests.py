from django.test import TestCase
from donation.models import Donation
import datetime

class DonationTestCase(TestCase):

    def setUp(self):
        Donation.objects.create(
            title = "donation",
            description = "donation",
            created_date = datetime.date.today(),
            amount = 50, 
            donor_name = "Jaime",
            donor_surname = "Moscoso",
            donor_dni = "12345678A",
            donor_address = "Sevilla",
            donor_email = "email@email.com"
        )

    def test_donation_create(self):
        donation = Donation.objects.get(title="donation")
        self.assertEqual(donation.title, "donation")
    
    def test_donation_create_incorrect_title_max(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
            title = "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
             + "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
            description = "donation",
            created_date = datetime.date.today(),
            amount = 50, 
            donor_name = "Jaime",
            donor_surname = "Moscoso",
            donor_dni = "12345678A",
            donor_address = "Sevilla",
            donor_email = "email@email.com"
            )
            
    def test_donation_create_incorrect_creation_date(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
            title = "donation",
            description = "donation",
            created_date = "INCORRECTO",
            amount = 50, 
            donor_name = "Jaime",
            donor_surname = "Moscoso",
            donor_dni = "12345678A",
            donor_address = "Sevilla",
            donor_email = "email@email.com"
            )

    def test_donation_create_incorrect_max_digits_amount(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
            title = "donation",
            description = "donation",
            created_date = datetime.date.today(),
            amount = 12345678901, 
            donor_name = "Jaime",
            donor_surname = "Moscoso",
            donor_dni = "12345678A",
            donor_address = "Sevilla",
            donor_email = "email@email.com"
            )

    def test_donation_create_incorrect_min_amount(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
            title = "donation",
            description = "donation",
            created_date = datetime.date.today(),
            amount = 0.01, 
            donor_name = "Jaime",
            donor_surname = "Moscoso",
            donor_dni = "12345678A",
            donor_address = "Sevilla",
            donor_email = "email@email.com"
            )
    def test_donation_create_incorrect_string_amount(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
            title = "donation",
            description = "donation",
            created_date = datetime.date.today(),
            amount = "Hola", 
            donor_name = "Jaime",
            donor_surname = "Moscoso",
            donor_dni = "12345678A",
            donor_address = "Sevilla",
            donor_email = "email@email.com"
            )

    def test_donation_create_incorrect_max_length_donor_name(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
            title = "donation",
            description = "donation",
            created_date = datetime.date.today(),
            amount = 50, 
            donor_name = "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
            donor_surname = "Moscoso",
            donor_dni = "12345678A",
            donor_address = "Sevilla",
            donor_email = "email@email.com"
            )

    def test_donation_create_incorrect_max_length_donor_surname(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
            title = "donation",
            description = "donation",
            created_date = datetime.date.today(),
            amount = 50, 
            donor_name = "Jaime",
            donor_surname = "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
            "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
            "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
            donor_dni = "12345678A",
            donor_address = "Sevilla",
            donor_email = "email@email.com"
            )

    def test_donation_create_incorrect_size_dni(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
            title = "donation",
            description = "donation",
            created_date = datetime.date.today(),
            amount = 10, 
            donor_name = "Jaime",
            donor_surname = "Moscoso",
            donor_dni = "123456789A",
            donor_address = "Sevilla",
            donor_email = "email@email.com"
            )

    def test_donation_create_incorrect_max_length_address(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
            title = "donation",
            description = "donation",
            created_date = datetime.date.today(),
            amount = 10, 
            donor_name = "Jaime",
            donor_surname = "Moscoso",
            donor_dni = "12345678A",
            donor_address = "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
            "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
            "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
            donor_email = "email@email.com"
            )

    def test_donation_create_incorrect_email(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
            title = "donation",
            description = "donation",
            created_date = datetime.date.today(),
            amount = 10, 
            donor_name = "Jaime",
            donor_surname = "Moscoso",
            donor_dni = "123456789A",
            donor_address = "Sevilla",
            donor_email = "email"
            )
    