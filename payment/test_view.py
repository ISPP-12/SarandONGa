from ong.models import Ong
from person.models import Worker
from .models import Payment, Project, GodFather

from datetime import datetime, timezone

from time import sleep

# SELENIUM IMPORTS
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentViewTestCase(StaticLiveServerTestCase):

    def setUp(self):
        super().setUp()
        self.usersuper = Worker(
            email="test@email.com",
            name="Test Person",
            surname="Test Apellido",
            birth_date=datetime(2001, 3, 14),
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
            payday=datetime(2023, 3, 11),
            amount=10,
            ong=self.ong,
            paid=True,
        )

        self.godfather = GodFather.objects.create(
            name='Johny',
            surname='Deep',
            dni='65004204T',
            email='emailje@gmail.com',
            birth_date=datetime(1990, 1, 24, tzinfo=timezone.utc),
            payment_method='T',
            bank_account_number='ES6621000418401234567198',
            bank_account_holder='John Bruh',
            bank_account_reference='1465 0100 72 2030876294',
            amount=100,
            frequency='M',
            start_date=datetime(2023, 1, 24, tzinfo=timezone.utc),
            termination_date=datetime(2024, 1, 24, tzinfo=timezone.utc),
            notes='Some notes',
            status='C', ong=self.ong
        )
        
        self.project = Project.objects.create(title="Título",
                                              country="Españita",
                                              start_date=datetime(
                                                  2023, 1, 3),
                                              end_date=datetime(
                                                  2024, 1, 3),
                                              number_of_beneficiaries=3,
                                              amount=15000,
                                              announcement_date=datetime(
                                                  2024, 1, 3),
                                              ong=self.ong)
        
        self.project2 = Project.objects.create(title="Título2",
                                                     country="España",
                                                     start_date=datetime(
                                                         2023, 1, 3),
                                                     end_date=datetime(
                                                         2024, 1, 3),
                                                     number_of_beneficiaries=3,
                                                     amount=15000,
                                                     announcement_date=datetime(
                                                         2024, 1, 3),
                                                     ong=self.ong)
        
        self.god_test = GodFather.objects.create(
            name='John',
            surname='Doe',
            dni='65004204V',
            email='emailja@gmail.com',
            birth_date=datetime(1990, 1, 24, tzinfo=timezone.utc),
            payment_method='T',
            bank_account_number='ES6621000418401234567891',
            bank_account_holder='John Doe',
            bank_account_reference='1465 0100 72 2030876293',
            amount=100,
            frequency='M',
            start_date=datetime(2023, 1, 24, tzinfo=timezone.utc),
            termination_date=datetime(2024, 1, 24, tzinfo=timezone.utc),
            notes='Some notes',
            status='S', ong=self.ong
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


    def test_payment_create_view_amount_error(self):
        before_count = Payment.objects.count()

        # Acess form from list
        self.driver.get(f"{self.live_server_url}/payment/create")

        # Fill and submit form (missing amount)
        self.driver.find_element(
            By.ID, "id_concept").send_keys("Pago Proyecto 2")

        # scroll to submit button and click
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        self.driver.find_element(By.ID, "submit").click()

        # Check there is no new payment
        after_count = Payment.objects.count()
        self.assertTrue(before_count == after_count)


    def test_payment_create_view_concept_error(self):
        before_count = Payment.objects.count()

        # Acess form from list
        self.driver.get(f"{self.live_server_url}/payment/create")

        # Fill and submit form (missing concept)
        self.driver.find_element(By.ID, "id_amount").send_keys("45")

        # scroll to submit button and click
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        self.driver.find_element(By.ID, "submit").click()

        # Check there is no new payment
        after_count = Payment.objects.count()
        self.assertTrue(before_count == after_count)


    def test_payment_create_view_negative_amount_error(self):
        before_count = Payment.objects.count()

        # Acess form from list
        self.driver.get(f"{self.live_server_url}/payment/create")

        # Fill and submit form (negative amount)
        self.driver.find_element(
            By.ID, "id_concept").send_keys("Pago Proyecto 2")
        self.driver.find_element(By.ID, "id_amount").send_keys("-45")

        # scroll to submit button and click
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        self.driver.find_element(By.ID, "submit").click()

        # Check there is no new payment
        after_count = Payment.objects.count()
        self.assertTrue(before_count == after_count)


    def test_payment_view_update(self):
        self.driver.get(
            f"{self.live_server_url}/payment/" +
            str(self.test_payment_1.id) + "/update"
        )

        concept = self.driver.find_element(
            By.ID, "id_concept").get_attribute("value")
        amount = self.driver.find_element(
            By.ID, "id_amount").get_attribute("value")
        payday = self.driver.find_element(
            By.ID, "id_payday").get_attribute("value")

        self.assertTrue(str(self.test_payment_1.concept) in concept)
        self.assertTrue(str(self.test_payment_1.amount) in amount)
        self.assertTrue(
            datetime.strptime(payday, "%Y-%m-%d") == self.test_payment_1.payday
        )

        # change concept
        new_concept = "Pago con otro concepto"
        self.driver.find_element(By.ID, "id_concept").clear()
        self.driver.find_element(By.ID, "id_concept").send_keys(new_concept)
        select = Select(self.driver.find_element(By.ID, 'id_project'))
        select.select_by_index(2)
        select2 = Select(self.driver.find_element(By.ID, 'id_godfather'))
        select2.select_by_index(1)
        # scroll to submit button and click
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        self.driver.find_element(By.ID, "submit").click()

        self.test_payment_1.refresh_from_db()
        self.assertTrue(self.test_payment_1.concept == new_concept)


    def test_payment_view_delete(self):
        self.driver.get(
            f"{self.live_server_url}/payment/" +
            str(self.test_payment_1.id) + "/update"
        )

        concept = self.driver.find_element(
            By.ID, "id_concept").get_attribute("value")
        amount = self.driver.find_element(
            By.ID, "id_amount").get_attribute("value")
        payday = self.driver.find_element(
            By.ID, "id_payday").get_attribute("value")

        self.assertTrue(str(self.test_payment_1.concept) in concept)
        self.assertTrue(str(self.test_payment_1.amount) in amount)
        self.assertTrue(
            datetime.strptime(payday, "%Y-%m-%d") == self.test_payment_1.payday
        )

        before_count = Payment.objects.count()

        # scroll to submit button and click
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        self.driver.find_element(By.ID, "delete").click()

        after_count = Payment.objects.count()
        self.assertTrue(before_count - 1 == after_count)


    def test_payment_view_exploratory_1(self):
        # check fix/730: PAYMENT FORM NOT MANTAINING SUBJECT

        # Acess form from list
        self.driver.get(f"{self.live_server_url}/user/godfather/list")
        self.driver.find_element(By.ID, f'card-list-item-{self.godfather.id}').click()
        # await until add-payment a is loaded
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-payment")))
        self.driver.find_element(By.ID, "add-payment").click()

        # Fill and submit form
        # await until the form is loaded
        print(self.driver.current_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_concept")))
        self.driver.find_element(By.ID, "id_concept").send_keys("Pago Padrino 1")
        self.driver.find_element(By.ID, "id_amount").send_keys("45")

        # scroll to submit button and click
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        # await until the button is loaded
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "submit")))
        self.driver.find_element(By.ID, "submit").click()

        # Check the url is correct
        correct_url = f"{self.live_server_url}/payment/create?godfather={self.godfather.id}"
        self.assertTrue(self.driver.current_url == correct_url)
        
        # Check godfather is selected
        select = Select(self.driver.find_element(By.ID, 'id_godfather'))
        self.assertTrue(self.godfather.name in select.first_selected_option.text)
