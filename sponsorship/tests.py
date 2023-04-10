from django.test import TestCase
from sponsorship.models import Sponsorship
from person.models import GodFather, Child
from home.models import Home
from ong.models import Ong
from datetime import datetime, date, timezone


class SponsorshipTestCase(TestCase):

    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        GodFather.objects.create(
            name='John',
            surname='Doe',
            dni='65004204V',
            email='emailja@gmail.com',
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

        Child.objects.create(email='test1@test.com', name='Test_1', surname='Test1 Test1', birth_date=datetime(2001, 6, 18),
                             sex="Femenino", city="Test1", address="Test1", telephone=123456789, postal_code=12345, photo="test1.jpg",
                             start_date=datetime(2006, 2, 23), termination_date=datetime(2020, 9, 12), educational_level="Test1", expected_mission_time="2",
                             mission_house="Test1", site="Test1", subsite="Test1", father_name="Dn. Test1", father_profession="Test1",
                             mother_name="Sra. Test1", mother_profession="Test1", number_brothers_siblings=3, correspondence="Test1", ong=self.ong)

        Home.objects.create(
            name='Casa Paco',
            payment_method='T',
            bank_account_number='ES6621000418401234567891',
            bank_account_holder='John Doe',
            bank_account_reference='1465 0100 72 2030876293',
            amount=100,
            frequency='M',
            start_date=datetime(2023, 1, 24, tzinfo=timezone.utc),
            termination_date=datetime(2024, 1, 24, tzinfo=timezone.utc),
        )

    def test_sponsorship_create_correct(self):
        god_test = GodFather.objects.get(email='emailja@gmail.com')
        child_test = Child.objects.get(email="test1@test.com")
        home_test = Home.objects.get(name='Casa Paco')

        sponsorship = Sponsorship(sponsorship_date=date.today(), termination_date=date.today(
        ), child=child_test, home=home_test)
        sponsorship.save()
        sponsorship.godfather.add(god_test)
        sponsorship.save()
        num_test = Sponsorship.objects.all().count()
        self.assertEqual(num_test, 1)

    def test_sponsorship_fail_child_null(self):
        home_test = Home.objects.get(name='Casa Paco')
        with self.assertRaises(Exception):
            sponsorship = Sponsorship(sponsorship_date=date.today(
            ), termination_date=date.today(), home=home_test)
            sponsorship.save()

    def test_sponsorship_fail_attributes_dateStart(self):
        god_test = GodFather.objects.get(email='emailja@gmail.com')
        child_test = Child.objects.get(email="test1@test.com")
        home_test = Home.objects.get(name='Casa Paco')

        with self.assertRaises(Exception):
            sponsorship = Sponsorship(sponsorship_date="prueba", termination_date=date.today(
            ), child=child_test, home=home_test, godfather=god_test)
            sponsorship.save()

    def test_sponsorship_fail_attributes_dateEnd(self):
        god_test = GodFather.objects.get(email='emailja@gmail.com')
        child_test = Child.objects.get(email="test1@test.com")
        home_test = Home.objects.get(name='Casa Paco')

        with self.assertRaises(Exception):
            sponsorship = Sponsorship(sponsorship_date=date.today(
            ), termination_date="prueba", child=child_test, home=home_test, godfather=god_test)
            sponsorship.save()

class SponsorshipUpdateTestCase(TestCase):

    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        GodFather.objects.create(
            name='John',
            surname='Doe',
            dni='65004204V',
            email='emailja@gmail.com',
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

        GodFather.objects.create(
            name='Jimmy',
            surname='Doe',
            dni='65004204A',
            email='emailja2@gmail.com',
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

        Child.objects.create(email='test1@test.com', name='Test_1', surname='Test1 Test1', birth_date=datetime(2001, 6, 18),
                             sex="Femenino", city="Test1", address="Test1", telephone=123456789, postal_code=12345, photo="test1.jpg",
                             start_date=datetime(2006, 2, 23), termination_date=datetime(2020, 9, 12), educational_level="Test1", expected_mission_time="2",
                             mission_house="Test1", site="Test1", subsite="Test1", father_name="Dn. Test1", father_profession="Test1",
                             mother_name="Sra. Test1", mother_profession="Test1", number_brothers_siblings=3, correspondence="Test1", ong=self.ong)
        
        Child.objects.create(email='test2@test.com', name='Test_1', surname='Test1 Test1', birth_date=datetime(2001, 6, 18),
                             sex="Femenino", city="Test1", address="Test1", telephone=123456789, postal_code=12345, photo="test1.jpg",
                             start_date=datetime(2006, 2, 23), termination_date=datetime(2020, 9, 12), educational_level="Test1", expected_mission_time="2",
                             mission_house="Test1", site="Test1", subsite="Test1", father_name="Dn. Test1", father_profession="Test1",
                             mother_name="Sra. Test1", mother_profession="Test1", number_brothers_siblings=3, correspondence="Test1", ong=self.ong)

        Home.objects.create(
            name='Casa Paco',
            payment_method='T',
            bank_account_number='ES6621000418401234567891',
            bank_account_holder='John Doe',
            bank_account_reference='1465 0100 72 2030876293',
            amount=100,
            frequency='M',
            start_date=datetime(2023, 1, 24, tzinfo=timezone.utc),
            termination_date=datetime(2024, 1, 24, tzinfo=timezone.utc),
        )

        Home.objects.create(
            name='Casa Pili',
            payment_method='T',
            bank_account_number='ES6621000418401234567891',
            bank_account_holder='John Doe',
            bank_account_reference='1465 0100 72 2030876293',
            amount=100,
            frequency='M',
            start_date=datetime(2023, 1, 24, tzinfo=timezone.utc),
            termination_date=datetime(2024, 1, 24, tzinfo=timezone.utc),
        )
        god_test = GodFather.objects.get(email='emailja@gmail.com')
        child_test = Child.objects.get(email="test1@test.com")
        home_test = Home.objects.get(name='Casa Paco')

        sponsorship = Sponsorship(sponsorship_date=date.today(), termination_date=date.today(
        ), child=child_test, home=home_test)
        sponsorship.save()
        sponsorship.godfather.add(god_test)
        sponsorship.save()

    def test_sponsorship_update_correct(self):
        god_test = GodFather.objects.get(email='emailja@gmail.com')
        god2_test = GodFather.objects.get(email='emailja2@gmail.com')
        child2_test = Child.objects.get(email="test2@test.com")
        home2_test = Home.objects.get(name='Casa Pili')
        sponsorship= Sponsorship.objects.get(godfather=god_test)
        sponsorship.sponsorship_date = date(2022, 1, 1)
        sponsorship.termination_date = date.today()
        sponsorship.child = child2_test
        sponsorship.home = home2_test
        sponsorship.godfather.add(god2_test)
        sponsorship.save()

    def test_sponsorship_update_incorrect_dates(self):
        god_test = GodFather.objects.get(email='emailja@gmail.com')
        sponsorship= Sponsorship.objects.get(godfather=god_test)
        with self.assertRaises(Exception):
            sponsorship.sponsorship_date = date.today()
            sponsorship.termination_date = date(2022, 1, 1)
            sponsorship.save()

    def test_sponsorship_update_incorrect_sponsorship_date(self):
        god_test = GodFather.objects.get(email='emailja@gmail.com')
        sponsorship= Sponsorship.objects.get(godfather=god_test)
        with self.assertRaises(Exception):
            sponsorship.sponsorship_date ="prueba"
            sponsorship.save()

    def test_sponsorship_update_incorrect_termination_date(self):
        god_test = GodFather.objects.get(email='emailja@gmail.com')
        sponsorship= Sponsorship.objects.get(godfather=god_test)
        with self.assertRaises(Exception):
            sponsorship.termination_date ="prueba"
            sponsorship.save()
