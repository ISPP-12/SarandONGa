from ong.models import Ong
from person.models import Worker
from person.models import ASEMUser

from datetime import datetime

from time import sleep

# SELENIUM IMPORTS
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AsemUserViewsTestCaseVidessur(StaticLiveServerTestCase):

    def setUp(self):
        super().setUp()

        self.ong = Ong(name='Asem')
        self.ong.save()

        self.test_asem_user_1 = ASEMUser(
            name="Test",
            surname="Test Apellido",
            birth_date=datetime(1990, 1, 24),
            condition="EM",
            member="EM",
            user_type="SACC",
            correspondence="E",
            status="C",
            family_unit_size=1,
            own_home="VC",
            bank_account_number="ES2831909938925888443384",
        )
        self.test_asem_user_1.ong = self.ong
        self.test_asem_user_1.save()

        self.usersuper = Worker(
            email="test@email.com",
            name="Test Person",
            surname="Test Apellido",
            birth_date=datetime(2001, 3, 14),
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
        self.driver.set_window_size(1920, 1080)

        self.driver.get(f'{self.live_server_url}/login/')
        self.driver.find_element(
            By.ID, "id_username").send_keys('test@email.com')
        self.driver.find_element(By.ID, "id_password").send_keys('adminTest')
        self.driver.find_element(By.ID, "id-submitForm").click()

    def tearDown(self):
        self.driver.quit()
        self.ong = None
        self.test_asem_user_1 = None
        self.usersuper = None
        super().tearDown()

    def test_asem_user_register_view(self):
        before_count = ASEMUser.objects.count()

        # Acess form from list
        self.driver.get(f'{self.live_server_url}/user/asem/list')
        sleep(1)
        self.driver.find_element(By.ID, "create-button").click()

        # Fill and submit form
        self.driver.find_element(By.ID, "id_name").send_keys("Andrés")
        self.driver.find_element(
            By.ID, "id_surname").send_keys("González García")
        self.driver.find_element(
            By.ID, "id_birth_date").send_keys("1990-01-24")
        Select(self.driver.find_element(
            By.ID, "id_condition")).select_by_index(1)
        Select(self.driver.find_element(By.ID, "id_member")).select_by_index(1)
        Select(self.driver.find_element(
            By.ID, "id_user_type")).select_by_index(1)
        Select(self.driver.find_element(
            By.ID, "id_correspondence")).select_by_index(1)
        Select(self.driver.find_element(By.ID, "id_status")).select_by_index(1)
        self.driver.find_element(By.ID, "id_family_unit_size").send_keys("3")
        Select(self.driver.find_element(
            By.ID, "id_own_home")).select_by_index(1)
        self.driver.find_element(By.ID, "id_bank_account_number").send_keys(
            "ES2831909938925888443384")

        # scroll to submit button and click
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        self.driver.find_element(By.ID, "submit").click()

        # Check there is one more user
        after_count = ASEMUser.objects.count()
        self.assertTrue(before_count == after_count-1)

    def test_asem_user_register_view_error(self):
        before_count = ASEMUser.objects.count()

        # Acess form from list
        self.driver.get(f'{self.live_server_url}/user/asem/list')

        self.driver.find_element(By.ID, "create-button").click()

        # Fill and submit form (missing name)
        self.driver.find_element(
            By.ID, "id_surname").send_keys("González García")
        Select(self.driver.find_element(
            By.ID, "id_condition")).select_by_index(1)
        Select(self.driver.find_element(By.ID, "id_member")).select_by_index(1)
        Select(self.driver.find_element(
            By.ID, "id_user_type")).select_by_index(1)
        Select(self.driver.find_element(
            By.ID, "id_correspondence")).select_by_index(1)
        Select(self.driver.find_element(By.ID, "id_status")).select_by_index(1)
        self.driver.find_element(By.ID, "id_family_unit_size").send_keys("3")
        Select(self.driver.find_element(
            By.ID, "id_own_home")).select_by_index(1)
        self.driver.find_element(By.ID, "id_bank_account_number").send_keys(
            "ES1234567890123456789012")

        # scroll to submit button and click
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        self.driver.find_element(By.ID, "submit").click()

        # Check there is no new user
        after_count = ASEMUser.objects.count()
        self.assertTrue(before_count == after_count)

    def test_asem_user_register_view_update(self):
        # Acess form from list
        self.driver.get(f'{self.live_server_url}/user/asem/list')
        self.assertTrue(self.driver.find_element(By.ID, "section-user"))

        # Check the test item appears
        test_user_div = self.driver.find_element(
            By.ID, f"card-list-item-{self.test_asem_user_1.id}")
        test_user_text = test_user_div.text
        self.assertTrue(str(self.test_asem_user_1.name) in test_user_text)
        self.assertTrue(str(self.test_asem_user_1.email)
                        in test_user_text or "-" in test_user_text)
        self.assertTrue(str(self.test_asem_user_1.telephone)
                        in test_user_text or "-" in test_user_text)
        self.assertTrue(str(self.test_asem_user_1.city)
                        in test_user_text or "-" in test_user_text)

        # Update item
        test_user_div.click()
        # await until update-button is visible and click
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "update-button")))
        self.driver.find_element(By.ID, "update-button").click()

        # change name
        new_name = "Andrés"
        self.driver.find_element(By.ID, "id_name").clear()
        self.driver.find_element(By.ID, "id_name").send_keys(new_name)

        # scroll to submit button and click
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        self.driver.find_element(By.ID, "submit").click()

        # Check the test item is updated in database
        self.test_asem_user_1.refresh_from_db()
        self.assertTrue(self.test_asem_user_1.name == new_name)

        # Check the test item is updated in view
        test_user_div = self.driver.find_element(
            By.ID, f"card-list-item-{self.test_asem_user_1.id}")
        test_user_text = test_user_div.text
        self.assertTrue(str(self.test_asem_user_1.name) in test_user_text)
        self.assertTrue(new_name in test_user_text)
