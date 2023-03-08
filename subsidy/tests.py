from django.test import TestCase

from subsidy.models import Subsidy

# Create your tests here.

class SubsidyTestCase(TestCase):
    def setUp(self):
        Subsidy.objects.create(date="2021-01-01", amount=1000, name="Juan")
        Subsidy.objects.create(date="2021-01-02", amount=2000, name="Pedro")
        Subsidy.objects.create(date="2021-01-03", amount=3000, name="Maria")
    
    def test_subsidy_create(self):
        subsidy = Subsidy.objects.get(name="Juan")
        self.assertEqual(subsidy.name, "Juan")
        self.assertEqual(subsidy.amount, 1000)
        self.assertEqual(subsidy.date, "2021-01-01")
    
    def test_subsidy_delete(self):
        subsidy = Subsidy.objects.get(name="Juan")
        subsidy.delete()
        self.assertEqual(Subsidy.objects.count(), 2)

    def test_subsidy_update(self):
        subsidy = Subsidy.objects.get(name="Juan")
        subsidy.name = "Juanito"
        subsidy.amount = 17
        subsidy.date = "2017-07-17"
        subsidy.save()
        self.assertEqual(subsidy.name, "Juanito")
        self.assertEqual(subsidy.amount, 17)
        self.assertEqual(subsidy.date, "2017-07-17")

    #Create test
    def test_subsidy_create_date_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(date="This is a date incorrect", amount=1000, name="Juan")

    def test_subsidy_create_amount_negative(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(date="2021-01-01", amount=-1000, name="Juan")
    
    def test_subsidy_create_name_max_length_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(date="2021-01-01", amount=1000, name="Juan"*100)
    
    def test_subsidy_create_name_blank(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(date="2021-01-01", amount=1000, name="")
    
    def test_subsidy_create_amount_null(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(date="2021-01-01", amount=None, name="Juan")
    
    def test_subsidy_create_date_null(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(date=None, amount=1000, name="Juan")
            
