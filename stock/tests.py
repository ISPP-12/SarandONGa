from django.db import transaction
from django.test import TestCase
from .models import Stock
from decimal import Decimal

class StockTestCase(TestCase):
    def setUp(self):
        self.stock1 = Stock.objects.create(name="Manzanas", quantity=4)
        self.stock2 = Stock.objects.create(name="Naranjas", quantity=7)
    
    def tearDown(self):
        Stock.objects.all().delete()

    def test_stock_create(self):
        count = Stock.objects.count()
        Stock.objects.create(name="Peras", quantity=9)
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
            
    def test_get_stock(self):
        stock = Stock.objects.create(name='Test Stock', quantity=100.00)
        retrieved_stock = Stock.objects.get(id=stock.id)
        self.assertEqual(retrieved_stock, stock)
        
    def test_get_nonexistent_stock(self):
        with self.assertRaises(Stock.DoesNotExist):
            Stock.objects.get(id=1000)
    
    @transaction.atomic        
    def test_create_stock_without_name(self):
        with self.assertRaises(Exception):
            Stock.objects.create(name=None,quantity=100.00)
    
    @transaction.atomic        
    def test_create_stock_without_quantity(self):
        with self.assertRaises(Exception):
            Stock.objects.create(name='Test Stock',quantity=None)



