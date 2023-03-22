from django.test import TestCase
from datetime import date, datetime
from .models import Home    

class HomeTestCase(TestCase):
    def setUp(self):
        Home.objects.create(name='Casa 1', payment_method='Transferencia',
                            bank_account_number= 'ES9021002220115629603391',
                            bank_account_holder='Marta', bank_account_reference='ES902',
                            amount=1, frequency='Anual', seniority=date(2006,2,23),
                            province='Sevilla', notes='Nada')
        Home.objects.create(name='Casa 2', payment_method='Tarjeta Bancaria',
                            bank_account_number= 'ES9021002220315629603391',
                            bank_account_holder='Jaime', bank_account_reference='ES90223',
                            amount=1, frequency='Trimestral', seniority=date(2012,2,23),
                            province='Cordoba', notes='Nada')
    
    def test_home_create(self):
        home = Home.objects.get(name='Casa 1')
        self.assertEqual(home.payment_method, 'Transferencia')
        self.assertEqual(home.bank_account_number, 'ES9021002220115629603391' )
        self.assertEqual(home.bank_account_holder, 'Marta')
        self.assertEqual(home.bank_account_reference,'ES902')    
        self.assertEqual(home.amount, 1)
        self.assertEqual(home.frequency, 'Anual')
        self.assertEqual(home.seniority,date(2006, 2, 23))
        self.assertEqual(home.province,'Sevilla')
        self.assertEqual(home.notes,'Nada')
        
        
        home2 = Home.objects.get(name='Casa 2')
        self.assertEqual(home2.payment_method, 'Tarjeta Bancaria')
        self.assertEqual(home2.bank_account_number, 'ES9021002220315629603391' )
        self.assertEqual(home2.bank_account_holder, 'Jaime')
        self.assertEqual(home2.bank_account_reference,'ES90223')    
        self.assertEqual(home2.amount, 1)
        self.assertEqual(home2.frequency, 'Trimestral')
        self.assertEqual(home2.seniority,date(2012, 2, 23))
        self.assertEqual(home2.province,'Cordoba')
        self.assertEqual(home2.notes,'Nada')
        
    def test_home_create_incorrect_name(self):
        with self.assertRaises(Exception):
            Home.objects.create(name='C'*26, payment_method='Transferencia',
                            bank_account_number= 'ES9021002220115629603391',
                            bank_account_holder='Marta', bank_account_reference='ES902',
                            amount=1, frequency='Anual', seniority=date(2006,2,23),
                            province='Sevilla', notes='Nada')
    
    def test_home_create_incorrect_payment_method(self):
        with self.assertRaises(Exception):
            Home.objects.create(name='Casa', 
                            payment_method='N'*51,
                            bank_account_number= 'ES9021002220115629603391',
                            bank_account_holder='Marta', bank_account_reference='ES902',
                            amount=1, frequency='Anual', seniority=date(2006,2,23),
                            province='Sevilla', notes='Nada')    
    
    
    def test_home_create_incorrect_bank_account_holder(self):
        with self.assertRaises(Exception):
            Home.objects.create(name='Casa', payment_method='Transferencia',
                            bank_account_number= 'ES9021002220115629603391',
                            bank_account_holder='M'*101, bank_account_reference='ES902',
                            amount=1, frequency='Anual', seniority=date(2006,2,23),
                            province='Sevilla', notes='Nada')            
            
    def test_home_create_incorrect_bank_account_reference(self):
        with self.assertRaises(Exception):
            Home.objects.create(name='Casa', payment_method='Transferencia',
                            bank_account_number= 'ES9021002220115629603391',
                            bank_account_holder='Marta', 
                            bank_account_reference='A'*101,
                            amount=1, frequency='Anual', seniority=date(2006,2,23),
                            province='Sevilla', notes='Nada') 
            
    def test_home_create_incorrect_amount(self):
        with self.assertRaises(Exception):
            Home.objects.create(name='Casa', payment_method='Transferencia',
                            bank_account_number= 'ES9021002220115629603391',
                            bank_account_holder='Marta', 
                            bank_account_reference='AS121',
                            amount=0, frequency='Anual', seniority=date(2006,2,23),
                            province='Sevilla', notes='Nada')     
            
    def test_home_create_incorrect_frequency(self):
        with self.assertRaises(Exception):
            Home.objects.create(name='Casa', payment_method='Transferencia',
                            bank_account_number= 'ES9021002220115629603391',
                            bank_account_holder='Marta', 
                            bank_account_reference='AS121',
                            amount=1, frequency='A'*21, seniority=date(2006,2,23),
                            province='Sevilla', notes='Nada')   
    
                    