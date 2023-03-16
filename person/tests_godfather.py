from datetime import datetime, timedelta, timezone
from django.test import TestCase
from person.models import GodFather

class GodFatherTestCase(TestCase):
    def setUp(self):
        GodFather.objects.create(
            name = 'John',
            surname = 'Doe',
            dni='65004204V',
            email = 'emailja@gmail.com',
            payment_method='T',
            bank_account_number='ES6621000418401234567891',
            bank_account_holder='John Doe',
            bank_account_reference='1465 0100 72 2030876293',
            amount = 100,
            frequency = 'M',
            seniority = datetime(2023, 1, 24, tzinfo=timezone.utc),
            notes = 'Some notes',
            status = 'S',
            )
        

        GodFather.objects.create(
            name = 'Johny',
            surname = 'Deep',
            dni='65004204T',
            email = 'emailje@gmail.com',
            payment_method='T',
            bank_account_number='ES6621000418401234567198',
            bank_account_holder='John Bruh',
            bank_account_reference='1465 0100 72 2030876294',
            amount = 100,
            frequency = 'M',
            seniority = datetime(2022, 1, 24, tzinfo=timezone.utc),
            notes = 'Some notes',
            status = 'C',
            )
        

        GodFather.objects.create(
            name = 'Juan',
            surname = 'Pérez',
            dni='65001204Z',
            email = 'emailjo@gmail.com',
            payment_method='T',
            bank_account_number='ES6621000418401234567176',
            bank_account_holder='Juan Pérez',
            bank_account_reference='1465 0100 72 2030876214',
            amount = 100,
            frequency = 'M',
            seniority = datetime(2021, 1, 24, tzinfo=timezone.utc),
            notes = 'Some notes',
            status = 'S',
            )
        

    def test_godfather_create(self):
        gf = GodFather.objects.get(dni='65004204V')
        self.assertEqual(gf.dni, '65004204V')
        self.assertEqual(gf.payment_method, 'T')
        self.assertEqual(gf.bank_account_number,'ES6621000418401234567891')
        self.assertEqual(gf.bank_account_holder, 'John Doe')
        self.assertEqual(gf.bank_account_reference, '1465 0100 72 2030876293')
        self.assertEqual(gf.amount, 100)
        self.assertEqual(gf.frequency, 'M')
        self.assertEqual(gf.seniority.strftime('%Y-%m-%d'), "2023-01-24")
        self.assertEqual(gf.notes, 'Some notes')
        self.assertEqual(gf.status, 'S')
        

        gf2 = GodFather.objects.get(dni='65004204T')
        self.assertEqual(gf2.dni, '65004204T')
        self.assertEqual(gf2.payment_method, 'T')
        self.assertEqual(gf2.bank_account_number,'ES6621000418401234567198')
        self.assertEqual(gf2.bank_account_holder, 'John Bruh')
        self.assertEqual(gf2.bank_account_reference, '1465 0100 72 2030876294')
        self.assertEqual(gf2.amount, 100)
        self.assertEqual(gf2.frequency, 'M')
        self.assertEqual(gf2.seniority.strftime('%Y-%m-%d'), "2022-01-24")
        self.assertEqual(gf2.notes, 'Some notes')
        self.assertEqual(gf2.status, 'C')
        

        gf3 = GodFather.objects.get(dni='65001204Z')
        self.assertEqual(gf3.dni, '65001204Z')
        self.assertEqual(gf3.payment_method, 'T')
        self.assertEqual(gf3.bank_account_number,'ES6621000418401234567176')
        self.assertEqual(gf3.bank_account_holder, 'Juan Pérez')
        self.assertEqual(gf3.bank_account_reference, '1465 0100 72 2030876214')
        self.assertEqual(gf3.amount, 100)
        self.assertEqual(gf3.frequency, 'M')
        self.assertEqual(gf3.seniority.strftime('%Y-%m-%d'), "2021-01-24")
        self.assertEqual(gf3.notes, 'Some notes')
        self.assertEqual(gf3.status, 'S')
        

    def test_godfather_update(self):
        godfather = GodFather.objects.get(dni='65004204V')
        godfather.amount = 200
        godfather.psyment_method = 'TB'
        godfather.bank_account_number = 'ES6621000418401234567890'
        godfather.bank_account_holder = 'John Doe 2'
        godfather.bank_account_reference = '1465 0100 72 2030876299'
        godfather.frequency = 'Y'
        godfather.seniority = datetime(2000, 1, 24, tzinfo=timezone.utc)
        godfather.notes = 'Some notes 2'
        godfather.status = 'C'
        godfather.save()

        self.assertEqual(godfather.amount, 200)
        self.assertEqual(godfather.payment_method, 'T')
        self.assertEqual(godfather.bank_account_number, 'ES6621000418401234567890')
        self.assertEqual(godfather.bank_account_holder, 'John Doe 2')
        self.assertEqual(godfather.bank_account_reference, '1465 0100 72 2030876299')
        self.assertEqual(godfather.frequency, 'Y')
        self.assertEqual(godfather.seniority.strftime('%Y-%m-%d'), "2000-01-24")
        self.assertEqual(godfather.notes, 'Some notes 2')
        self.assertEqual(godfather.status, 'C')
        

    def test_godfather_delete(self):
        godfather = GodFather.objects.get(dni='65004204V')
        godfather.delete()
        self.assertEqual(GodFather.objects.count(), 2)

    def test_gf_incorrect_seniority(self):
        gf = GodFather.objects.get(dni='65004204T')
        gf.seniority = datetime.now() + timedelta(days=1)
        with self.assertRaises(Exception):
            gf.save()
            gf.full_clean()

    def test_godfather_bank_account_number_incorrect_max(self):
        with self.assertRaises(Exception):
            GodFather.objects.create(email="tcamerob2@gmail.com",
            name="Tomas2",
            surname='Camero',
            amount = 100,
            frequency = 'M',
            seniority = datetime(2021, 1, 24, tzinfo=timezone.utc),
            payment_method = 'T',
            bank_account_number="ES11111111111111111111111")
        
    def test_gf_incorrect_bank_number(self):
        
        with self.assertRaises(Exception):
            gf = GodFather.objects.get(dni='65004204T')
            gf.bank_account_number = "E11111111111111111111111111"
            gf.full_clean()  
            gf.save()
                 


    def test_gf_incorrect_bank_holder(self):
        gf = GodFather.objects.get(dni='65004204T')
        gf.bank_account_holder = 1
        with self.assertRaises(Exception):
            gf.save()
            gf.full_clean()

    def test_gf_incorrect_bank_reference(self):
        gf = GodFather.objects.get(dni='65004204T')
        gf.bank_account_reference = 'i'*20
        with self.assertRaises(Exception):
            gf.save()
            gf.full_clean()

    def test_gf_incorrect_amount(self):
        gf = GodFather.objects.get(dni='65004204T')
        gf.amount = -1
        with self.assertRaises(Exception):
            gf.save()
            gf.full_clean()

    def test_gf_incorrect_frequency(self):
        gf = GodFather.objects.get(dni='65004204T')
        gf.frequency = 'AAAA'
        with self.assertRaises(Exception):
            gf.save()
            gf.full_clean()

    def test_gf_incorrect_status(self):
        gf = GodFather.objects.get(dni='65004204T')
        gf.status = 'AAAA'
        with self.assertRaises(Exception):
            gf.save()
            gf.full_clean()

    def test_gf_incorrect_payment_method(self):
        gf = GodFather.objects.get(dni='65004204T')
        gf.payment_method = 'AAAA'
        with self.assertRaises(Exception):
            gf.save()
            gf.full_clean()

    def test_gf_incorrect_dni(self):
        gf = GodFather.objects.get(dni='65004204T')
        gf.dni = 'AAAA'
        with self.assertRaises(Exception):
            gf.save()
            gf.full_clean()
