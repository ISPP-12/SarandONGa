from django.test import TestCase
from donation.models import Donation
import datetime
from ong.models import Ong
from person.models import Worker

# SELENIUM IMPORTS
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class DonationTestCase(TestCase):

    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        Donation.objects.create(
            title="donation",
            description="donation",
            created_date=datetime.date.today(),
            amount=50,
            donor_name="Jaime",
            donor_surname="Moscoso",
            donor_dni="12345678A",
            donor_address="Sevilla",
            donor_email="email@email.com",
            document="",
            ong=self.ong
        )

    def test_donation_create(self):
        donation = Donation.objects.get(title="donation")
        self.assertEqual(donation.title, "donation")

    def test_donation_update(self):
        donation = Donation.objects.get(title="donation")
        donation.title = "change"
        donation.description = "change"
        donation.created_date = datetime.date(2023, 3, 4)
        donation.amount = 12
        donation.donor_name = "change"
        donation.donor_surname = "change"
        donation.donor_dni = "66666666A"
        donation.donor_address = "change"
        donation.donor_email = "change@email.com"
        self.assertEqual(donation.title, "change")
        self.assertEqual(donation.description, "change")
        self.assertEqual(donation.created_date, datetime.date(2023, 3, 4))
        self.assertEqual(donation.amount, 12)
        self.assertEqual(donation.donor_name, "change")
        self.assertEqual(donation.donor_surname, "change")
        self.assertEqual(donation.donor_dni, "66666666A")
        self.assertEqual(donation.donor_address, "change")
        self.assertEqual(donation.donor_email, "change@email.com")

    def test_donation_delete(self):
        donation = Donation.objects.get(title="donation")
        self.assertEqual(Donation.objects.count(), 1)
        donation.delete()
        self.assertEqual(Donation.objects.count(), 0)

    def test_donation_create_incorrect_title_max(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
                + "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
                description="donation",
                created_date=datetime.date.today(),
                amount=50,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_creation_date(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date="INCORRECTO",
                amount=50,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_max_digits_amount(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=12345678901,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_min_amount(self):
        with self.assertRaises(Exception):
            donation = Donation(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=0.01,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )
            donation.full_clean()
            donation.save()

    def test_donation_create_incorrect_string_amount(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount="Hola",
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_max_length_donor_name(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=50,
                donor_name="iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_max_length_donor_surname(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=50,
                donor_name="Jaime",
                donor_surname="iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
                "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
                "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
                donor_dni="12345678A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_size_dni(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=10,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="123456789A",
                donor_address="Sevilla",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_max_length_address(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=10,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="12345678A",
                donor_address="iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
                "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
                "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
                donor_email="email@email.com",
                ong=self.ong
            )

    def test_donation_create_incorrect_email(self):
        with self.assertRaises(Exception):
            Donation.objects.create(
                title="donation",
                description="donation",
                created_date=datetime.date.today(),
                amount=10,
                donor_name="Jaime",
                donor_surname="Moscoso",
                donor_dni="123456789A",
                donor_address="Sevilla",
                donor_email="email",
                ong=self.ong
            )

    def test_donation_update_incorrect_title_max(self):
        donation = Donation.objects.get(title="donation")
        donation.title = "donation"*50
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_title_max(self):
        donation = Donation.objects.get(title="donation")
        donation.title = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_blank_title_max(self):
        donation = Donation.objects.get(title="donation")
        donation.title = ""
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_creation_date(self):
        donation = Donation.objects.get(title="donation")
        donation.created_date = "bad_date"
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_creation_date(self):
        donation = Donation.objects.get(title="donation")
        donation.created_date = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_max_digits_amount(self):
        donation = Donation.objects.get(title="donation")
        donation.amount = 10000000000
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_amount(self):
        donation = Donation.objects.get(title="donation")
        donation.amount = "bad_amount"
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_max_digits_amount(self):
        donation = Donation.objects.get(title="donation")
        donation.amount = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_min_amount(self):
        donation = Donation.objects.get(title="donation")
        donation.amount = -1
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_max_length_donor_name(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_name = "Pedro"*50
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_blank_donor_name(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_name = ""
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_donor_name(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_name = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_max_length_donor_surname(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_surname = "Pedro"*250
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_blank_donor_surname(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_surname = ""
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_donor_surname(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_surname = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_size_dni(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_dni = "26"*7
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_size_dni(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_dni = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_blank_size_dni(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_dni = ""
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_size_address(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_address = "Address"*200
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_incorrect_email(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_email = "email"
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_null_email(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_email = None
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()

    def test_donation_update_blank_email(self):
        donation = Donation.objects.get(title="donation")
        donation.donor_email = ""
        with self.assertRaises(Exception):
            donation.full_clean()
            donation.save()


# SELENIUM TESTS
class DonationListViewTestCaseAsem(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()

        self.ong = Ong(name='ASEM')
        self.test_donation_1 = Donation(title="donation", description='some description here', amount=100, donor_name="Pedro",
                                        donor_surname="Perez", donor_dni="12345678A", donor_address="Calle 1", donor_email="pedroperez@donor.com", ong=self.ong)

        self.ong.save()
        self.test_donation_1.save()

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
        self.test_donation_1 = None
        super().tearDown()

    def test_access_donation_view(self):
        # Check access
        self.driver.get(f'{self.live_server_url}/donation/list')
        self.assertTrue(self.driver.find_element(By.ID, "section-donation"))

    #     # Check the test item appears
        test_donation_div = self.driver.find_element(
            By.ID, f"donation-{self.test_donation_1.id}")
        test_donation_text = test_donation_div.find_element(
            By.CSS_SELECTOR, "h5").text
        spans = test_donation_div.find_element(
            By.CLASS_NAME, "row").find_elements(By.TAG_NAME, "span")
        self.assertTrue(test_donation_text == self.test_donation_1.title)
        # Comento este test porque el navegador devuelve la fecha usando el locale y cambia para cada equipo
        # self.assertTrue(spans[0].text == self.test_donation_1.created_date.strftime("%d/%m/%Y %H:%M"))
        self.assertIn(str(self.test_donation_1.amount), spans[1].text)
        self.assertTrue(spans[2].text == self.test_donation_1.donor_email)

        #     #Check the left section is still empty
        left_section_div = self.driver.find_element(By.ID, "preview")
        self.assertTrue(left_section_div.find_element(
            By.ID, "prev-info").text == "Pulsa sobre una donación para la vista previa")

        # Check the item div is clickable
        test_donation_div.click()

        # Now the preview section should be filled with the test item data
        children = left_section_div.find_elements(By.CSS_SELECTOR, "h2, p")
        self.assertTrue(children[0].text == self.test_donation_1.title)
        self.assertTrue(children[1].text == self.test_donation_1.description)
        # 100 € is the text in the html
        self.assertTrue(children[2].text == "Cantidad: " +
                        str(self.test_donation_1.amount) + " €")
        self.assertTrue(children[3].text == "Nombre donante: " +
                        self.test_donation_1.donor_name + " " + self.test_donation_1.donor_surname)
        self.assertTrue(
            children[4].text == "DNI donante: " + self.test_donation_1.donor_dni)
        self.assertTrue(
            children[5].text == "Dirección donante: " + self.test_donation_1.donor_address)
        self.assertTrue(
            children[6].text == "Correo donante: " + self.test_donation_1.donor_email)

    def test_delete_donation_view(self):
        # Check access
        self.driver.get(f'{self.live_server_url}/donation/list')
        self.assertTrue(self.driver.find_element(By.ID, "section-donation"))

    #     # Check the test item appears
        test_donation_div = self.driver.find_element(
            By.ID, f"donation-{self.test_donation_1.id}")
        test_donation_text = test_donation_div.find_element(
            By.CSS_SELECTOR, "h5").text
        spans = test_donation_div.find_element(
            By.CLASS_NAME, "row").find_elements(By.TAG_NAME, "span")
        self.assertTrue(test_donation_text == self.test_donation_1.title)
        # Comento este test porque el navegador devuelve la fecha usando el locale y cambia para cada equipo
        # self.assertTrue(spans[0].text == self.test_donation_1.created_date.strftime("%d/%m/%Y %H:%M"))
        self.assertIn(str(self.test_donation_1.amount), spans[1].text)
        self.assertTrue(spans[2].text == self.test_donation_1.donor_email)

        #     #Check the left section is still empty
        left_section_div = self.driver.find_element(By.ID, "preview")
        self.assertTrue(left_section_div.find_element(
            By.ID, "prev-info").text == "Pulsa sobre una donación para la vista previa")

        # Check the item div is clickable
        test_donation_div.click()

        # Check the item is removed
        before_count = Donation.objects.count()
        lateral_btns = self.driver.find_element(By.ID, "lateralButtons")
        delete_btn = lateral_btns.find_elements(By.TAG_NAME, "a")[1]
        delete_btn.click()
        after_count = Donation.objects.count()

        self.assertTrue(before_count == after_count+1)
