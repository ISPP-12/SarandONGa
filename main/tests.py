from ong.models import Ong
from person.models import Worker
import datetime

# SELENIUM IMPORTS
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class PricingPlanTestCase(StaticLiveServerTestCase):
    def setUp(self):
      super().setUp()
      self.ong = Ong(name='ASEM')
      self.ong.save()

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
      super().tearDown()

    def test_pricing_plan_exploratory(self):
       #Check access
      self.driver.get(f'{self.live_server_url}')
      self.assertTrue(self.driver.find_element(By.CLASS_NAME, "demo"))

      #Check there are two plans
      pricing = self.driver.find_element(By.CLASS_NAME, "demo").find_element(By.CLASS_NAME, "demo").find_elements(By.CLASS_NAME, "pricingTable")
      self.assertEqual(len(pricing), 2)

      #Check pricing plan: we should have the standard adquired
      container1 = pricing[0].find_element(By.CLASS_NAME, "pricingTable-sign-up")
      self.assertEqual(container1.text, "ADQUIRIDO")

      # #Check pricing plan: we should have the contract button on the premium plan
      container2 = pricing[1].find_element(By.CLASS_NAME, "pricingTable-sign-up")
      self.assertEqual(container2.find_element(By.TAG_NAME, "button").find_element(By.TAG_NAME, "span").text, "Contratar")

      self.ong.plan = 'P'
      self.ong.premium_payment_date = datetime.date.today()
      self.ong.save()

      self.superuser.ong = self.ong
      self.superuser.save()
      #wait untill the premium plan is adquired
      self.driver.get(f'{self.live_server_url}')
      #Check pricing plan: we should have the premium adquired
      pricing = self.driver.find_element(By.CLASS_NAME, "demo").find_element(By.CLASS_NAME, "demo").find_elements(By.CLASS_NAME, "pricingTable")
      container2 = pricing[1].find_element(By.CLASS_NAME, "pricingTable-sign-up")

      self.assertEqual(container2.find_element(By.TAG_NAME, "span").text, "ADQUIRIDO")

      # now we have to check that there are no contract buttons or adquired text on standard plan
      container1 = pricing[0].find_element(By.CLASS_NAME, "pricingTable-sign-up")
      self.assertEqual(container1.text, "")