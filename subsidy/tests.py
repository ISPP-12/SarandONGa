from django.test import TestCase
from ong.models import Ong

from subsidy.models import Subsidy
import datetime
from time import sleep
from person.models import Worker

# SELENIUM IMPORTS
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class SubsidyTestCase(TestCase):
    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                               provisional_resolution="2021-01-02", final_resolution="2021-01-03", amount=1000, name="Juan", ong=self.ong, status="Presentada")
        Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG2",
                               provisional_resolution="2021-01-03", final_resolution="2021-01-04", amount=1000, name="Pedro", ong=self.ong, status="Presentada")
        Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG3",
                               provisional_resolution="2021-01-07", final_resolution="2021-01-08", amount=1000, name="Maria", ong=self.ong, status="Presentada")

    def test_subsidy_create(self):
        subsidy = Subsidy.objects.get(name="Juan")
        self.assertEqual(subsidy.name, "Juan")
        self.assertEqual(subsidy.amount, 1000)
        self.assertEqual(str(subsidy.presentation_date), "2021-01-01")
        self.assertEqual(str(subsidy.payment_date), "2021-01-02")
        self.assertEqual(str(subsidy.provisional_resolution), "2021-01-02")
        self.assertEqual(str(subsidy.final_resolution), "2021-01-03")
        self.assertEqual(subsidy.organism, "ONG1")
        self.assertEqual(subsidy.ong.name, "Mi ONG")

    def test_subsidy_delete(self):
        subsidy = Subsidy.objects.get(name="Juan")
        subsidy.delete()
        self.assertEqual(Subsidy.objects.count(), 2)

    def test_subsidy_update(self):
        subsidy = Subsidy.objects.get(name="Juan")
        subsidy.name = "Juanito"
        subsidy.amount = 17
        subsidy.presentation_date = "2017-07-17"
        subsidy.payment_date = "2017-07-18"
        subsidy.provisional_resolution = "2017-07-18"
        subsidy.final_resolution = "2017-07-19"
        subsidy.organism = "ONG4"
        subsidy.save()
        self.assertEqual(subsidy.name, "Juanito")
        self.assertEqual(subsidy.amount, 17)
        self.assertEqual(str(subsidy.presentation_date), "2017-07-17")
        self.assertEqual(str(subsidy.payment_date), "2017-07-18")
        self.assertEqual(str(subsidy.provisional_resolution), "2017-07-18")
        self.assertEqual(str(subsidy.final_resolution), "2017-07-19")
        self.assertEqual(subsidy.organism, "ONG4")

    # Create test
    def test_subsidy_create_presentation_date_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="This is a date incorrect", payment_date="2021-01-02", organism="ONG2",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Pedro", ong=self.ong)

    def test_subsidy_create_presentation_justification_date_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01",presentation_justification_date="This is a date incorrect", payment_date="2021-01-02", organism="ONG2",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Pedro", ong=self.ong)

    def test_subsidy_create_payment_date_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="This is a date incorrect", organism="ONG2",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Pedro", ong=self.ong)

    def test_create_subsidy_organism_max_length_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG2"*100,
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Pedro", ong=self.ong)

    def test_subsidy_create_amount_negative(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG2",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=-1000, name="Pedro", ong=self.ong)

    def test_subsidy_create_name_max_length_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Juan"*1000, ong=self.ong)

    def test_subsidy_create_name_null(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name=None, ong=self.ong)

    def test_subsidy_create_amount_null(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=None, name="Juan", ong=self.ong)

    def test_subsidy_create_organism_null(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism=None,
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Juan", ong=self.ong)

    def test_subsidy_create_final_resolution_before_provisional(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG2",provisional_resolution="2017-07-19", final_resolution="2017-07-18", amount=1000, name="Pedro",ong=self.ong)

    def test_subsidy_create_status_max_length_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Juan"*1000, ong=self.ong, status="P"*51)

    def test_subsidy_create_status_null(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Juan"*1000, ong=self.ong, status=None)

    def test_subsidy_create_status_blank(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Juan"*1000, ong=self.ong, status="")

# TESTS UPDATE SUBSIDY

    def test_incorrect_amount_null(self):
            with self.assertRaises(Exception):
                self.subsidy.amount = None
                self.subsidy.save()

    def test_incorrect_amount_negative(self):
            with self.assertRaises(Exception):
                self.subsidy.amount = -1000
                self.subsidy.save()
    
    def test_incorrect_amount_string(self):
            with self.assertRaises(Exception):
                self.subsidy.amount = "Juan"
                self.subsidy.save()

    def test_incorrect_amount_bool(self):
            with self.assertRaises(Exception):
                self.subsidy.amount = True
                self.subsidy.save()
    
    def test_incorrect_payment_date_value_string_format(self):
            with self.assertRaises(Exception):
                self.subsidy.payment_date = "2010-23-12"
                self.subsidy.save()

    def test_incorrect_payment_date_value_string_format2(self):
            with self.assertRaises(Exception):
                self.subsidy.payment_date = "23/12/23"
                self.subsidy.save()

    def test_incorrect_payment_date_value_string_format3(self):
            with self.assertRaises(Exception):
                self.subsidy.payment_date = "23-12-23"
                self.subsidy.save()
    
    def test_incorrect_organism_null(self):
            with self.assertRaises(Exception):
                self.subsidy.organism = None
                self.subsidy.save()

    def test_incorrect_organism_max_length(self):
            with self.assertRaises(Exception):
                self.subsidy.organism = "ONG2"*100
                self.subsidy.save()

    def test_incorrect_name_null(self):
            with self.assertRaises(Exception):
                self.subsidy.name = None
                self.subsidy.save()

    def test_incorrect_name_max_length(self):
            with self.assertRaises(Exception):
                self.subsidy.name = "Juan"*1000
                self.subsidy.save()

    def test_incorrect_final_resolution_before_provisional(self):
            with self.assertRaises(Exception):
                self.subsidy.provisional_resolution = "2017-07-17"
                self.subsidy.final_resolution = "2017-07-18"
                self.subsidy.save()

    def test_incorrect_presentation_justification_date_before_presentation_date(self):
        with self.assertRaises(Exception):
            self.subsidy.presentation_justification_date = "2017-07-17"
            self.subsidy.presentation_date = "2017-07-18"
            self.subsidy.save()

    def test_incorrect_ong_null(self):
            with self.assertRaises(Exception):
                self.subsidy.ong = None
                self.subsidy.save()
    
    def test_incorrect_ong_value(self):
            with self.assertRaises(Exception):
                self.subsidy.ong = "ONG1"
                self.subsidy.save()

class SubsidyListViewTestCaseAsem(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()

        self.ong = Ong(name='ASEM')
        self.test_subsidy_1 = Subsidy(presentation_date=datetime.date(2022,12,4),
                                      payment_date=datetime.date(2023,5,1),
                                      organism='Spanish State',
                                      provisional_resolution=datetime.date(2023,3,24),
                                      final_resolution=datetime.date(2023,4,1),
                                      amount=12000.0,
                                      name='Test Subsidy 1',
                                      status='Por presentar',
                                      ong=self.ong)

        self.ong.save()
        self.test_subsidy_1.save()

        self.superuser = Worker(
            email="test@email.com",
            name="Test Person",
            surname="Test Apellido",
            birth_date=datetime.datetime(
                2001, 3, 14, tzinfo=datetime.timezone.utc),
            sex='M',
            city='Test City',
            address='Test Street',
            telephone='123456789',
            postal_code='41012',
        )
        self.superuser.ong = self.ong
        self.superuser.set_password('root')
        self.superuser.is_admin = True
        self.superuser.save()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)

        self.driver.get(f'{self.live_server_url}/login/')
        self.driver.find_element(
            By.ID, "id_username").send_keys('test@email.com')
        self.driver.find_element(By.ID, "id_password").send_keys('root')
        self.driver.find_element(By.ID, "id-submitForm").click()

    def tearDown(self):
        self.driver.quit()
        self.ong = None
        self.test_subsidy_1 = None
        super().tearDown()

    def test_access_subsidy_view(self):
        # Check access
        self.driver.get(f'{self.live_server_url}/subsidy/list')
        self.assertTrue(self.driver.find_element(By.ID, "section-subsidy"))

        # Check the test item appears
        test_subsidy_div = self.driver.find_element(
            By.ID, f"subsidy-{self.test_subsidy_1.id}")
        test_subsidy_text = test_subsidy_div.find_element(
            By.CSS_SELECTOR, "h5").text
        spans = test_subsidy_div.find_element(
            By.CLASS_NAME, "row").find_elements(By.TAG_NAME, "span")
        self.assertTrue(test_subsidy_text == self.test_subsidy_1.name)
        self.assertTrue(spans[0].text.strip() == self.test_subsidy_1.organism)
        self.assertIn(str(self.test_subsidy_1.status), spans[1].text)

        #  Check the left section is still empty
        left_section_div = self.driver.find_element(By.ID, "preview")
        self.assertTrue(len(left_section_div.find_elements(By.CLASS_NAME, "row")) == 0)

        # Check the item div is clickable
        test_subsidy_div.click()

        # Now the preview section should be filled with the test item data
        children = left_section_div.find_elements(By.CSS_SELECTOR, "h2, p")
        self.assertTrue(children[0].text == self.test_subsidy_1.name)
        self.assertTrue(children[1].find_element(By.TAG_NAME,'span').text == self.test_subsidy_1.organism)
        self.assertTrue(children[2].text == "Cantidad: " +
                        str(int(self.test_subsidy_1.amount)).replace(".",",") + " €")
        # The rest of the attributes won't be tested until the display 
        # for null values is fixed


    def test_delete_subsidy_view(self):
        # Check access
        self.driver.get(f'{self.live_server_url}/subsidy/list')
        self.assertTrue(self.driver.find_element(By.ID, "section-subsidy"))

        # Check the test item appears
        test_subsidy_div = self.driver.find_element(
            By.ID, f"subsidy-{self.test_subsidy_1.id}")
        test_subsidy_text = test_subsidy_div.find_element(
            By.CSS_SELECTOR, "h5").text
        spans = test_subsidy_div.find_element(
            By.CLASS_NAME, "row").find_elements(By.TAG_NAME, "span")
        self.assertTrue(test_subsidy_text == self.test_subsidy_1.name)
        self.assertTrue(spans[0].text.strip() == self.test_subsidy_1.organism)
        self.assertIn(str(self.test_subsidy_1.status), spans[1].text)

        # Check the left section is still empty
        left_section_div = self.driver.find_element(By.ID, "preview")
        self.assertTrue(len(left_section_div.find_elements(By.CLASS_NAME, "row")) == 0)

        # Check the item div is clickable
        test_subsidy_div.click()

        # Check the item is removed
        before_count = Subsidy.objects.count()
        lateral_btns = self.driver.find_element(By.ID, "lateralButtons")
        delete_btn = lateral_btns.find_elements(By.TAG_NAME, "a")[1]
        delete_btn.click()

        confirmation = self.driver.switch_to.alert
        confirmation.accept()
        sleep(1)

        after_count = Subsidy.objects.count()

        self.assertTrue(before_count == after_count+1)           

