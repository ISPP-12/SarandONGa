from datetime import datetime, timezone
from django.test import TestCase
from ong.models import Ong
from person.models import GodFather

class GodFatherTestCase(TestCase):
    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        self.god_test = GodFather.objects.create(
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
            start_date = datetime(2023, 1, 24, tzinfo=timezone.utc),
            termination_date = datetime(2024, 1, 24, tzinfo=timezone.utc),
            notes = 'Some notes',
            status = 'S',ong=self.ong
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
            start_date = datetime(2023, 1, 24, tzinfo=timezone.utc),
            termination_date = datetime(2024, 1, 24, tzinfo=timezone.utc),
            notes = 'Some notes',
            status = 'C',ong=self.ong
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
            start_date = datetime(2023, 1, 24, tzinfo=timezone.utc),
            termination_date = datetime(2024, 1, 24, tzinfo=timezone.utc),
            notes = 'Some notes',
            status = 'S',ong=self.ong
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
        self.assertEqual(gf.start_date.strftime('%Y-%m-%d'), "2023-01-24")
        self.assertEqual(gf.termination_date.strftime('%Y-%m-%d'), "2024-01-24")
        self.assertEqual(gf.notes, 'Some notes')
        self.assertEqual(gf.status, 'S')
        self.assertEqual(gf.ong, self.ong)
        

        gf2 = GodFather.objects.get(dni='65004204T')
        self.assertEqual(gf2.dni, '65004204T')
        self.assertEqual(gf2.payment_method, 'T')
        self.assertEqual(gf2.bank_account_number,'ES6621000418401234567198')
        self.assertEqual(gf2.bank_account_holder, 'John Bruh')
        self.assertEqual(gf2.bank_account_reference, '1465 0100 72 2030876294')
        self.assertEqual(gf2.amount, 100)
        self.assertEqual(gf2.frequency, 'M')
        self.assertEqual(gf.start_date.strftime('%Y-%m-%d'), "2023-01-24")
        self.assertEqual(gf.termination_date.strftime('%Y-%m-%d'), "2024-01-24")
        self.assertEqual(gf2.notes, 'Some notes')
        self.assertEqual(gf2.status, 'C')
        self.assertEqual(gf2.ong, self.ong)
        

        gf3 = GodFather.objects.get(dni='65001204Z')
        self.assertEqual(gf3.dni, '65001204Z')
        self.assertEqual(gf3.payment_method, 'T')
        self.assertEqual(gf3.bank_account_number,'ES6621000418401234567176')
        self.assertEqual(gf3.bank_account_holder, 'Juan Pérez')
        self.assertEqual(gf3.bank_account_reference, '1465 0100 72 2030876214')
        self.assertEqual(gf3.amount, 100)
        self.assertEqual(gf3.frequency, 'M')
        self.assertEqual(gf.start_date.strftime('%Y-%m-%d'), "2023-01-24")
        self.assertEqual(gf.termination_date.strftime('%Y-%m-%d'), "2024-01-24")
        self.assertEqual(gf3.notes, 'Some notes')
        self.assertEqual(gf3.status, 'S')
        self.assertEqual(gf3.ong, self.ong)
        

    def test_godfather_update(self):
        godfather = GodFather.objects.get(dni='65004204V')
        godfather.amount = 200
        godfather.payment_method = 'TB'
        godfather.bank_account_number = 'ES6621000418401234567890'
        godfather.bank_account_holder = 'John Doe 2'
        godfather.bank_account_reference = '1465 0100 72 2030876299'
        godfather.frequency = 'Y'
        godfather.birth_date = datetime(1990, 1, 24, tzinfo=timezone.utc)
        godfather.start_date = datetime(2000, 1, 24, tzinfo=timezone.utc)
        godfather.termination_date = datetime(2010, 1, 24, tzinfo=timezone.utc)
        godfather.notes = 'Some notes 2'
        godfather.status = 'C'
        godfather.save()

        self.assertEqual(godfather.amount, 200)
        self.assertEqual(godfather.payment_method, 'TB')
        self.assertEqual(godfather.bank_account_number, 'ES6621000418401234567890')
        self.assertEqual(godfather.bank_account_holder, 'John Doe 2')
        self.assertEqual(godfather.bank_account_reference, '1465 0100 72 2030876299')
        self.assertEqual(godfather.frequency, 'Y')
        self.assertEqual(godfather.start_date.strftime('%Y-%m-%d'), "2000-01-24")
        self.assertEqual(godfather.termination_date.strftime('%Y-%m-%d'), "2010-01-24")
        self.assertEqual(godfather.notes, 'Some notes 2')
        self.assertEqual(godfather.status, 'C')
        

    def test_godfather_delete(self):
        godfather = GodFather.objects.get(dni='65004204V')
        godfather.delete()
        self.assertEqual(GodFather.objects.count(), 2)

    def test_godfather_bank_account_number_incorrect_max(self):
        with self.assertRaises(Exception):
            godfather = GodFather.objects.create(email="tcamerob2@gmail.com",
            name="Tomas2",
            surname='Camero',
            amount = 100,
            frequency = 'M',
            payment_method = 'T',
            bank_account_number="ES" + "1" * 23,
            ong=self.ong)
            godfather.full_clean()

        
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


 # TESTS UPDATE godfather 

    def test_godfather_update_incorrect_name_max_lenght(self):
        godfather = GodFather.objects.get(name="Johny")
        godfather.name = "a"*201
        with self.assertRaises(Exception):
            godfather.save()
    
    def test_godfather_update_incorrect_name_null(self):
        godfather = GodFather.objects.get(name="Johny")
        godfather.name = None
        with self.assertRaises(Exception):
            godfather.save()
    
    def test_godfather_incorrect_name_int(self):
        with self.assertRaises(Exception):
                self.god_test.name = 123
                self.god_test.save()
                self.god_test.full_clean()

    def test_godfather_update_incorrect_surname_max_lenght(self):
        godfather = GodFather.objects.get(name="Johny")
        godfather.surname = "a"*201
        with self.assertRaises(Exception):
            godfather.save()
    
    def test_godfather_update_incorrect_surname_null(self):
        godfather = GodFather.objects.get(name="Johny")
        godfather.surname = None
        with self.assertRaises(Exception):
            godfather.save()
            self.god_test.full_clean()

    def test_godfather_incorrect_surname_int(self):
        with self.assertRaises(Exception):
                self.god_test_update.surname = 123
                self.god_test_update.save()
                self.god_test_update.full_clean()
    
    def test_godfather_incorrect_email(self):
        with self.assertRaises(Exception):
                self.god_test_update.email = "emailfalso"
                self.god_test_update.save()
                self.god_test_update.full_clean()
    
    def test_godfather_incorrect_birth_date(self):
            with self.assertRaises(Exception):
                self.god_test_update.birth_date = "23-12-23"
                self.god_test_update.save()
                self.god_test_update.full_clean()
    
    def test_godfather_incorrect_sex(self):
            with self.assertRaises(Exception):
                self.god_test_update.sex = "J"
                self.god_test_update.save()
                self.god_test_update.full_clean()
    
    def test_incorrect_city(self):
            with self.assertRaises(Exception):
                self.god_test_update.city = 1111
                self.god_test_update.save()
                self.god_test_update.full_clean()

    def test_incorrect_city_max_length(self):
        godfather = GodFather.objects.get(name="Johny")
        godfather.city = "a"*201
        with self.assertRaises(Exception):
            godfather.save()
            
            
    
    def test_incorrect_addres_max_length(self):
        godfather = GodFather.objects.get(name="Johny")
        godfather.address = "a"*201
        with self.assertRaises(Exception):
            godfather.save()
    
    def test_incorrect_telephone(self):
        with self.assertRaises(Exception):
                self.god_test.telephone = "a"
                self.god_test.save()
                self.god_test.full_clean()
    
    def test_incorrect_cellphone(self):
            with self.assertRaises(Exception):
                self.god_test_update.telephone = "11111111111111111111111111111111111111111111111111111111111"
                self.god_test_update.save()
                self.god_test_update.full_clean()
    
    def test_incorrect_postal_code(self):
        godfather = GodFather.objects.get(name="Johny")
        godfather.postal_code = "a"*52
        with self.assertRaises(Exception):
            godfather.save()
    
    def test_incorrect_postal_code(self):
            with self.assertRaises(Exception):
                self.god_test_update.posta_code = "J"
                self.god_test_update.save()
                self.god_test_update.full_clean()

   
    def test_incorrect_start_date(self):
        with self.assertRaises(Exception):
            self.god_test.start_date = "23-12-23"
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_incorrect_dni(self):
        with self.assertRaises(Exception):
            self.god_test.dni = "29533919"
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_incorrect_dni_null(self):
        with self.assertRaises(Exception):
            self.god_test.dni = None
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_incorrect_dni_max_length(self):
        with self.assertRaises(Exception):
            self.god_test.dni = "29533919"
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_incorrect_amount_null(self):
        with self.assertRaises(Exception):
            self.god_test.amount = None
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_incorrect_amount_negative(self):
        with self.assertRaises(Exception):
            self.god_test.amount = -1
            self.god_test.save()
            self.god_test.full_clean()
    
    
    def test_incorrect_bank_reference_null(self):
        with self.assertRaises(Exception):
            self.god_test.bank_account_reference = None
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_incorrect_bank_account_null(self):
        with self.assertRaises(Exception):
            self.god_test.bank_account = None
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_godfather_update_bank_account_number_incorrect_blank(self):
        with self.assertRaises(Exception):
            self.god_test.bank_account_number = ""
            self.god_test.full_clean()    
    
 
    def test_incorrect_status_null(self):
        with self.assertRaises(Exception):
            self.god_test.status = None
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_incorrect_status_int(self):
        with self.assertRaises(Exception):
            self.god_test.status = 111
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_incorrect_status_string(self):
        with self.assertRaises(Exception):
            self.god_test.status = "111"
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_incorrect_frequency_null(self):
        with self.assertRaises(Exception):
            self.god_test.frequency = None
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_incorrect_frequency_choice(self):
        with self.assertRaises(Exception):
            self.god_test.frequency = "JJJJJ"
            self.god_test.save()
            self.god_test.full_clean()
    
    
    def test_incorrect_ong_null(self):
        with self.assertRaises(Exception):
            self.god_test.ong = None
            self.god_test.save()
            self.god_test.full_clean()

    def test_incorrect_ong_int(self):
        with self.assertRaises(Exception):
            self.god_test.ong = 111
            self.god_test.save()
            self.god_test.full_clean()
    
    def test_incorrect_ong_string(self):
        with self.assertRaises(Exception):
            self.god_test.ong = "111"
            self.god_test.save()
            self.god_test.full_clean()