import datetime
from django.test import TestCase
from ong.models import Ong
from person.models import Worker


class WorkerTestCase(TestCase):

    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        Worker.objects.create(email="worker1@gmail.com",
                              name="Worker1",
                              surname="Worker1",
                              birth_date=datetime.datetime(
                                  1998, 3, 12, tzinfo=datetime.timezone.utc),
                              sex="Masculino",
                              city="Sevilla",
                              address="Reina Mercedes 11",
                              telephone=666666666,
                              postal_code=41013,
                              photo="",
                              is_active=True,
                              is_admin=True,
                              ong=self.ong)

        Worker.objects.create(email="worker2@gmail.com",
                              name="Worker2",
                              surname="Worker2",
                              birth_date=datetime.datetime(
                                  1998, 3, 12, tzinfo=datetime.timezone.utc),
                              sex="Masculino",
                              city="Sevilla",
                              address="Triana 16",
                              telephone=666666666,
                              postal_code=41015,
                              photo="",
                              is_active=True,
                              is_admin=True,
                              ong=self.ong)

    def test_worker_create(self):
        worker = Worker.objects.get(name="Worker1")
        self.assertEqual(worker.name, "Worker1")
        self.assertEqual(worker.surname, "Worker1")
        self.assertEqual(worker.birth_date.strftime('%Y-%m-%d'), "1998-03-12")
        self.assertEqual(worker.sex, "Masculino")

    def test_worker_delete(self):
        worker = Worker.objects.get(name="Worker1")
        self.assertEqual(Worker.objects.count(), 2)
        worker.delete()
        self.assertEqual(Worker.objects.count(), 1)

    def test_worker_update(self):
        worker = Worker.objects.get(name="Worker2")
        worker.name = "Update"
        worker.surname = "Change"
        worker.sex = "Femenino"
        worker.city = "Badajoz"
        worker.address = "Menachos"
        worker.birth_date = datetime.datetime(
            2003, 6, 14, tzinfo=datetime.timezone.utc)
        worker.telephone = 654654654
        worker.postal_code = 41004
        worker.photo = ""
        worker.is_active = False
        worker.is_admin = False
        worker.save()
        self.assertEqual(worker.name, "Update")
        self.assertEqual(worker.surname, "Change")
        self.assertEqual(worker.birth_date.strftime(
            '%Y-%m-%d'), "2003-06-14")
        self.assertEqual(worker.sex, "Femenino")
        self.assertEqual(worker.city, "Badajoz")
        self.assertEqual(worker.address, "Menachos")
        self.assertEqual(worker.telephone, 654654654)
        self.assertEqual(worker.postal_code, 41004)
        self.assertEqual(worker.photo, "")
        self.assertEqual(worker.is_active, False)
        self.assertEqual(worker.is_admin, False)

    def test_worker_create_name_incorrect_max(self):
        with self.assertRaises(Exception):
            Worker.objects.create(email="worker2@gmail.com",
                                  name="Worker2"*50,
                                  surname="Worker2",
                                  birth_date=datetime.datetime(
                                      1998, 3, 12, tzinfo=datetime.timezone.utc),
                                  sex="Masculino",
                                  city="Sevilla",
                                  address="Triana 16",
                                  telephone=666666666,
                                  postal_code=41015,
                                  photo="",
                                  is_active=True,
                                  is_admin=True,ong=self.ong)

    def test_worker_create_name_incorrect_null(self):
        with self.assertRaises(Exception):
            Worker.objects.create(email="worker2@gmail.com",
                                  name=None,
                                  surname="Worker2",
                                  birth_date=datetime.datetime(
                                      1998, 3, 12, tzinfo=datetime.timezone.utc),
                                  sex="Masculino",
                                  city="Sevilla",
                                  address="Triana 16",
                                  telephone=666666666,
                                  postal_code=41015,
                                  photo="",
                                  is_active=True,
                                  is_admin=True,ong=self.ong)

    def test_worker_create_email_incorrect(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="bad_email",
                                           name="Worker2",
                                           surname="Worker2",
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino",
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone=666666666,
                                           postal_code=41015,
                                           photo="",
                                           is_active=True,
                                           is_admin=True,ong=self.ong)
            worker.full_clean()

    def test_worker_create_email_incorrect_null(self):
        with self.assertRaises(Exception):
            Worker.objects.create(email=None,
                                  name="Worker2",
                                  surname="Worker2",
                                  birth_date=datetime.datetime(
                                      1998, 3, 12, tzinfo=datetime.timezone.utc),
                                  sex="Masculino",
                                  city="Sevilla",
                                  address="Triana 16",
                                  telephone=666666666,
                                  postal_code=41015,
                                  photo="",
                                  is_active=True,
                                  is_admin=True,ong=self.ong)

    def test_worker_create_surname_incorrect_null(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname=None,
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino",
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone=666666666,
                                           postal_code=41015,
                                           photo="",
                                           is_active=True,
                                           is_admin=True,ong=self.ong)
            worker.full_clean()

    def test_worker_create_surname_incorrect_max(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2"*50,
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino",
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone=666666666,
                                           postal_code=41015,
                                           photo="",
                                           is_active=True,
                                           is_admin=True,ong=self.ong)
            worker.full_clean()

    def test_worker_create_birth_date_incorrect(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2"*50,
                                           birth_date="bad_date",
                                           sex="Masculino",
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone=666666666,
                                           postal_code=41015,
                                           photo="",
                                           is_active=True,
                                           is_admin=True,ong=self.ong)
            worker.full_clean()

    def test_worker_create_sex_incorrect_max(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2"*50,
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino"*50,
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone=666666666,
                                           postal_code=41015,
                                           photo="",
                                           is_active=True,
                                           is_admin=True,ong=self.ong)
            worker.full_clean()

    def test_worker_create_sex_incorrect(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2"*50,
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="bad_sex",
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone=666666666,
                                           postal_code=41015,
                                           photo="",
                                           is_active=True,
                                           is_admin=True,ong=self.ong)
            worker.full_clean()

    def test_worker_create_city_incorrect_max(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2"*50,
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino",
                                           city="Sevilla"*200,
                                           address="Triana 16",
                                           telephone=666666666,
                                           postal_code=41015,
                                           photo="",
                                           is_active=True,
                                           is_admin=True,ong=self.ong)
            worker.full_clean()

    def test_worker_create_address_incorrect(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2"*50,
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino",
                                           city="Sevilla",
                                           address="Triana 16"*200,
                                           telephone=666666666,
                                           postal_code=41015,
                                           photo="",
                                           is_active=True,
                                           is_admin=True,ong=self.ong)
            worker.full_clean()

    def test_worker_create_telephone_incorrect(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2"*50,
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino",
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone="bad_telephone",
                                           postal_code=41015,
                                           photo="",
                                           is_active=True,
                                           is_admin=True,ong=self.ong)
            worker.full_clean()

    def test_worker_create_postal_code_incorrect(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2"*50,
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino",
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone=666666666,
                                           postal_code="bad_postal_code",
                                           photo="",
                                           is_active=True,
                                           is_admin=True,ong=self.ong)
            worker.full_clean()
