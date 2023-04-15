from datetime import date
from time import sleep
import datetime
from ong.models import Ong
from .models import Volunteer,Worker
# SELENIUM IMPORTS
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class UserListViewTestCaseVidessur(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()
        
        self.ong = Ong(name='VidesSur')
        self.ong.save()

        self.test_volunteer_1 =  Volunteer(
            name='John',
            surname='Smith',
            email='johnsmith@gmail.com',
            dni='12345678Z',
            job='Developer',
            dedication_time=10,
            contract_start_date=date(2023, 1, 20),
            contract_end_date=date(2023, 2, 5),
            birth_date=date(1990, 1, 20),
            raffle=False,
            lottery=False,
            telephone='123456789',
            city='Madrid',
            is_member=False,
            pres_table=False,
            is_contributor=False,
            notes='This is a note',
            entity='Entity',
            table='Table',
            volunteer_type='Otro',
            ong=self.ong
        )
       
        self.test_volunteer_2 =  Volunteer(
            name='Gabriel',
            surname='Moreno',
            email='gabrimoreno@gmail.com',
            dni='23456781Z',
            job='Developer',
            dedication_time=10,
            contract_start_date=date(2023, 1, 20),
            contract_end_date=date(2023, 2, 5),
            birth_date=date(1990, 1, 20),
            raffle=False,
            lottery=False,
            city="Sevilla",
            telephone='123456489',
            is_member=False,
            pres_table=False,
            is_contributor=False,
            notes='This is a note',
            entity='Entity',
            table='Table',
            volunteer_type='Otro',
            ong=self.ong
        )
        

        self.test_volunteer_1.save()
        self.test_volunteer_2.save()


        self.usersuper = Worker(
            email="test@email.com",
            name="Test Person",
            surname="Test Apellido",
            birth_date=datetime.datetime(2001,3,14),
            sex='F',
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
        self.test_volunteer_1 = None
        self.test_volunteer_2 = None
        super().tearDown()

    def test_access_volunteer_view(self):
        # Check access
        self.driver.get(f'{self.live_server_url}/user/volunteer/list')
        volunteer_div=self.driver.find_element(By.ID,f"card-list-item-{self.test_volunteer_2.id}")
        self.assertTrue(volunteer_div)

        # Check the test item appears
        #test_volunteer_email = volunteer_div.find_element(By.CSS_SELECTOR,"div.col-email").text
        #self.assertTrue(test_volunteer_email == self.test_volunteer_2.email)
        #test_volunteer_phone = volunteer_div.find_element(By.CSS_SELECTOR,"div.col-telephone").text
        #self.assertTrue(test_volunteer_phone == self.test_volunteer_2.telephone)
        #test_volunteer_city = volunteer_div.find_element(By.CSS_SELECTOR,"div.col-city").text
        #self.assertTrue(test_volunteer_city == self.test_volunteer_2.city)

    
    def test_delete_volunteer_view(self):
        # Check access
        self.driver.get(f'{self.live_server_url}/user/volunteer/list')
        volunteer_div=self.driver.find_element(By.ID,"section-volunteer")

        # Check the test item appears
        volunteer_div=self.driver.find_element(By.ID,f"card-list-item-{self.test_volunteer_2.id}")
     
        self.assertTrue(volunteer_div)
        volunteer_div.click()

        # Check the item is removed
        before_count = Volunteer.objects.count()
        self.driver.find_element(By.ID,"delete-button").click()

        confirmation = self.driver.switch_to.alert
        confirmation.accept()
        sleep(1)

        after_count = Volunteer.objects.count()
        self.assertTrue(before_count == after_count+1 )
    
