from django.db import transaction
from django.test import TestCase

from ong.models import Ong
from .models import Stock
from decimal import Decimal
from person.models import Worker

from datetime import datetime

# SELENIUM IMPORTS
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class StockTestCase(TestCase):
    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        self.stock1 = Stock.objects.create(name="Manzanas", quantity=4,amount=3.0,ong=self.ong)
        self.stock2 = Stock.objects.create(name="Naranjas", quantity=7,amount=3.0,ong=self.ong)
    
    def tearDown(self):
        Stock.objects.all().delete()

    def test_stock_create(self):
        count = Stock.objects.count()
        Stock.objects.create(name="Peras",amount=3.0, quantity=9,ong=self.ong)
        new_count = Stock.objects.count()
        self.assertEqual(new_count, count+1)
    
    def test_stock_read(self):
        Stock.objects.get(name="Manzanas")
        self.assertEqual(self.stock1.quantity, 4)

    def test_stock_delete(self):
        count = Stock.objects.count()
        stock = Stock.objects.get(name="Manzanas")
        stock.delete()
        new_count = Stock.objects.count()
        self.assertEqual(new_count, count-1)

    def test_stock_update(self):
        stock = Stock.objects.get(name="Naranjas")
        stock.name = "Mandarinas"
        stock.quantity = 10
        stock.save()
        updated_stock = Stock.objects.get(pk=stock.id)
        self.assertEqual(updated_stock.name, "Mandarinas")
        self.assertEqual(updated_stock.quantity, 10)
    
    def test_quantity_decimal_numbers(self):
        stock = Stock.objects.get(name="Manzanas")
        self.assertEqual(stock.quantity, 4.00)

        stock.quantity = 4.199999
        stock.save()

        updated_stock = Stock.objects.get(name="Manzanas")
        self.assertEqual(updated_stock.quantity, Decimal('4.20'))

    def test_amount_decimal_numbers(self):
        stock = Stock.objects.get(name="Manzanas")
        self.assertEqual(stock.amount, 3.00)

        stock.amount = 3.199999
        stock.save()

        updated_stock = Stock.objects.get(name="Manzanas")
        self.assertEqual(updated_stock.amount, Decimal('3.20'))
    
    @transaction.atomic         
    def test_get_stock(self):
        stock = Stock.objects.create(name='Test Stock', amount=3.0,quantity=100.00,ong=self.ong)
        retrieved_stock = Stock.objects.get(id=stock.id)
        self.assertEqual(retrieved_stock, stock)
        
    def test_get_nonexistent_stock(self):
        with self.assertRaises(Stock.DoesNotExist):
            Stock.objects.get(id=1000)
    
    @transaction.atomic        
    def test_create_stock_without_name(self):
        with self.assertRaises(Exception):
            Stock.objects.create(name=None,amount=3.0,quantity=100.00)
    
    @transaction.atomic        
    def test_create_stock_without_quantity(self):
        with self.assertRaises(Exception):
            Stock.objects.create(name='Test Stock',amount=3.0,quantity=None)

    @transaction.atomic        
    def test_create_stock_without_amount(self):
        with self.assertRaises(Exception):
            Stock.objects.create(name='Test Stock',amount=None,quantity=100.00)

    @transaction.atomic 
    def test_create_name_max(self):
        with self.assertRaises(Exception):
            Stock.objects.create(name='a'*201,amount=3.0,quantity=100.00)
    
    @transaction.atomic 
    def test_create_name_blank(self):
        with self.assertRaises(Exception):
            s = Stock.objects.create(name='',amount=3.0,quantity=100.00)
            s.full_clean()
     
    @transaction.atomic        
    def test_create_quantity_max(self):
        with self.assertRaises(Exception):
            s = Stock.objects.create(name='Test Stock',amount=3.0,quantity=10000000000000)
            s.full_clean()
            
    @transaction.atomic 
    def test_create_quantity_min(self):
        with self.assertRaises(Exception):
            s = Stock.objects.create(name='Test Stock',amount=3.0,quantity=-1)
            s.full_clean()
            
    @transaction.atomic         
    def test_create_quantity_blank(self):
        with self.assertRaises(Exception):
            s = Stock.objects.create(name='Test Stock',amount=3.0,quantity='')
            s.full_clean()
            
    @transaction.atomic         
    def test_create_quantity_string(self):
        with self.assertRaises(Exception):
            s = Stock.objects.create(name='Test Stock',amount=3.0,quantity='a')
            s.full_clean()

    @transaction.atomic        
    def test_create_amount_max(self):
        with self.assertRaises(Exception):
            s = Stock.objects.create(name='Test Stock',amount=10000000000000,quantity=100.00)
            s.full_clean()

    @transaction.atomic 
    def test_create_amount_min(self):
        with self.assertRaises(Exception):
            s = Stock.objects.create(name='Test Stock',amount=-1,quantity=100.00)
            s.full_clean()
            
    @transaction.atomic         
    def test_create_amount_blank(self):
        with self.assertRaises(Exception):
            s = Stock.objects.create(name='Test Stock',amount='',quantity=100.00)
            s.full_clean()
            
    @transaction.atomic         
    def test_create_amount_string(self):
        with self.assertRaises(Exception):
            s = Stock.objects.create(name='Test Stock',amount='a',quantity=100.00)
            s.full_clean()
            
    @transaction.atomic         
    def test_update_name_null(self):
        with self.assertRaises(Exception):
            s = Stock.objects.get(name="Naranjas")
            s.stock.name = None
            s.full_clean()
    
    @transaction.atomic 
    def test_update_name_max(self):
        with self.assertRaises(Exception):
            stock = Stock.objects.get(name="Naranjas")
            stock.name = 'a'*201
            stock.full_clean()
    
    @transaction.atomic         
    def test_update_name_blank(self):
        with self.assertRaises(Exception):
            stock = Stock.objects.get(name="Naranjas")
            stock.name = ''
            stock.full_clean()
    
    @transaction.atomic         
    def test_update_quantity_null(self):
        with self.assertRaises(Exception):
            stock = Stock.objects.get(name="Naranjas")
            stock.quantity = None
            stock.full_clean()
    
    @transaction.atomic         
    def test_update_quantity_max(self):
        with self.assertRaises(Exception):
            stock = Stock.objects.get(name="Naranjas")
            stock.quantity = 10000000000000
            stock.full_clean()
    
    @transaction.atomic         
    def test_update_quantity_string(self):
        with self.assertRaises(Exception):
            stock = Stock.objects.get(name="Naranjas")
            stock.quantity = 'a'
            stock.full_clean()
            
    @transaction.atomic         
    def test_update_quantity_min(self):
        with self.assertRaises(Exception):
            stock = Stock.objects.get(name="Naranjas")
            stock.quantity = -1
            stock.full_clean()
    
    @transaction.atomic         
    def test_update_amount_max(self):
        with self.assertRaises(Exception):
            stock = Stock.objects.get(name="Naranjas")
            stock.amount = 10000000000000
            stock.full_clean()
    
    @transaction.atomic         
    def test_update_amount_string(self):
        with self.assertRaises(Exception):
            stock = Stock.objects.get(name="Naranjas")
            stock.amount = 'a'
            stock.full_clean()
            
    @transaction.atomic         
    def test_update_amount_min(self):
        with self.assertRaises(Exception):
            stock = Stock.objects.get(name="Naranjas")
            stock.amount = -1
            stock.full_clean()

class StockListViewTestCaseVidessur(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()
        
        self.ong = Ong(name='VidesSur')
        self.test_stock_1 = Stock(name="Test stock 1",amount=3.0, ong=self.ong, quantity=150)

        self.ong.save()
        self.test_stock_1.save()

        self.usersuper = Worker(
            email="test@email.com",
            name="Test Person",
            surname="Test Apellido",
            birth_date=datetime(2001,3,14,1),
            sex='M',
            city='Test Ciudad',
            address='Test Calle',
            telephone='123456789',
            postal_code='41010',
        )
        self.usersuper.ong = self.ong
        self.usersuper.set_password('adminTest')
        self.usersuper.is_admin = True
        self.usersuper.save()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920,1080)

        self.driver.get(f'{self.live_server_url}/login/')
        self.driver.find_element(By.ID,"id_username").send_keys('test@email.com')
        self.driver.find_element(By.ID,"id_password").send_keys('adminTest')
        self.driver.find_element(By.ID,"id-submitForm").click()


    def tearDown(self):
        self.driver.quit()
        self.ong = None
        self.test_stock_1 = None
        super().tearDown()

    def test_access_stock_view(self):
        # Check access
        self.driver.get(f'{self.live_server_url}/stock/list')
        self.assertTrue(self.driver.find_element(By.ID,"section-stock"))

        # Check the test item appears
        test_stock_div = self.driver.find_element(By.ID,f"id-productDiv-{self.test_stock_1.id}")
        test_stock_text = test_stock_div.find_element(By.CSS_SELECTOR,"h5.card-title span").text
        self.assertTrue(test_stock_text == self.test_stock_1.name)

        # Check the display change
        self.driver.find_element(By.ID,"id-toList").click()
        self.assertTrue(self.driver
                        .find_element(By.ID,f"id-productDiv-{self.test_stock_1.id}")
                        .find_element(By.CLASS_NAME,"card-stock-list"))
        self.driver.find_element(By.ID,"id-toGrid").click()
        self.assertTrue(self.driver
                        .find_element(By.ID,f"id-productDiv-{self.test_stock_1.id}")
                        .find_element(By.CLASS_NAME,"card-stock"))
        
    def test_delete_stock_view(self):
        # Check access
        self.driver.get(f'{self.live_server_url}/stock/list')
        self.assertTrue(self.driver.find_element(By.ID,"section-stock"))

        # Check the test item appears
        test_stock_div = self.driver.find_element(By.ID,f"id-productDiv-{self.test_stock_1.id}")
        test_stock_text = test_stock_div.find_element(By.CSS_SELECTOR,"h5.card-title span").text
        self.assertTrue(test_stock_text == self.test_stock_1.name)

        # Check the item is removed
        before_count = Stock.objects.count()
        test_stock_div.find_element(By.ID,f"id-delete-{self.test_stock_1.id}").click()
        after_count = Stock.objects.count()

        self.assertTrue(before_count == after_count+1 )
    def test_stock_register_view(self):
        # Check access
        before_count = Stock.objects.count()
       
        self.driver.get(f'{self.live_server_url}/stock/list')
        self.driver.find_element(By.ID,"create-button").click()
        self.driver.find_element(By.ID,"id_name").send_keys("Lápiz bic azul")
        self.driver.find_element(By.ID,"id_quantity").send_keys("100")
        self.driver.find_element(By.ID,"id_amount").send_keys("30")
        self.driver.find_element(By.ID,"submit").click()
        after_count = Stock.objects.count()
        self.assertTrue(before_count == after_count-1 )

    def test_stock_register_view_error(self):
        # Check access
        before_count = Stock.objects.count()
       
        self.driver.get(f'{self.live_server_url}/stock/list')
        self.driver.find_element(By.ID,"create-button").click()
        self.driver.find_element(By.ID,"id_name").send_keys("Lápiz bic azul")
        self.driver.find_element(By.ID,"id_quantity").send_keys("-100")
        self.driver.find_element(By.ID,"submit").click()
        after_count = Stock.objects.count()
        self.assertTrue(before_count == after_count )

    def test_stock_register_view_update(self):
        self.driver.get(f'{self.live_server_url}/stock/list')
        self.assertTrue(self.driver.find_element(By.ID,"section-stock"))

        # Check the test item appears
        test_stock_div = self.driver.find_element(By.ID,f"id-productDiv-{self.test_stock_1.id}")
        test_stock_text = test_stock_div.find_element(By.CSS_SELECTOR,"h5.card-title span").text
        self.assertTrue(test_stock_text == self.test_stock_1.name)

        #Update item
        test_stock_div.find_element(By.ID,f"id-update-{self.test_stock_1.id}").click()
        self.driver.find_element(By.ID,"id_name").clear()
        self.driver.find_element(By.ID,"id_name").send_keys("Lápiz bic rojo")
        self.driver.find_element(By.ID,"submit").click()

        # Check the test item appears
        test_stock_div = self.driver.find_element(By.ID,f"id-productDiv-{self.test_stock_1.id}")
        test_stock_text = test_stock_div.find_element(By.CSS_SELECTOR,"h5.card-title span").text
        self.assertTrue(test_stock_text == "Lápiz bic rojo")






        
