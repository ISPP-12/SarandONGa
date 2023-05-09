# SELENIUM IMPORTS
from time import sleep
import datetime
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from home.models import Home
from ong.models import Ong
from payment.models import Payment

from person.models import Worker

class HomeViewTestCase(StaticLiveServerTestCase):

    def setUp(self):
        super().setUp()
        self.usersuper = Worker(
            email="test@email.com",
            name="Test Person",
            surname="Test Apellido",
            birth_date=datetime.datetime(2001, 3, 14),
            sex="M",
            city="Test Ciudad",
            address="Test Calle",
            telephone="123456789",
            postal_code="41010",
        )

        self.ong = Ong.objects.create(name="VidesSur")
        self.usersuper.ong = self.ong
        self.test_payment_1 = Payment(
            concept="concept",
            payday=datetime.datetime(2023, 3, 11),
            amount=10,
            ong=self.ong,
            paid=True,
        )

        self.home = Home.objects.create(
            name='Johny',
            payment_method='T',
            bank_account_number='ES6621000418401234567198',
            bank_account_holder='John Bruh',
            bank_account_reference='1465 0100 72 2030876294',
            amount=100,
            frequency='M',
            start_date=datetime.datetime(2023, 1, 24, tzinfo=datetime.timezone.utc),
            termination_date=datetime.datetime(2024, 1, 24, tzinfo=datetime.timezone.utc),
            notes='Some notes',
        )
        
        
        
        self.test_payment_1.save()
        self.usersuper.set_password("adminTest")
        self.usersuper.is_admin = True
        self.usersuper.save()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)

        self.driver.get(f"{self.live_server_url}/login/")
        self.driver.find_element(
            By.ID, "id_username").send_keys("test@email.com")
        self.driver.find_element(By.ID, "id_password").send_keys("adminTest")
        self.driver.find_element(By.ID, "id-submitForm").click()


    def tearDown(self):
        self.driver.quit()
        self.ong = None
        self.test_payment_1 = None
        self.usersuper = None
        self.god_test = None
        self.project2 = None
        self.project2 = None
        super().tearDown()

    def test_home_view_exploratory_1(self):
        # check fix/730: PAYMENT FORM NOT MANTAINING SUBJECT

        # Acess form from list
        self.driver.get(f"{self.live_server_url}/home/list")
        # await until add-payment a is loaded


        
        self.driver.find_element(By.ID, "id_amount_min").click()
        self.driver.find_element(By.ID, "id_amount_min").send_keys("80")
        self.driver.find_element(By.ID, "id-filter").click()
        url_before = self.driver.current_url
        
        self.driver.find_element(By.XPATH, "//h5[contains(.,\'Johny\')]").click()
        self.driver.find_element(By.ID, "delete-button").click()
        
        self.driver.switch_to.alert.accept()
        url_after = self.driver.current_url
        print(url_after)
        print(url_before)
        assert url_before == url_after
