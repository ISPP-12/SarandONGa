import datetime
from django.test import TestCase
from ong.models import Ong
from person.models import Worker
from django.urls import reverse
from unittest.mock import patch


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
                              telephone="666666666",
                              postal_code="41013",
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
                              telephone="666666666",
                              postal_code="41015",
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
        self.assertEqual(worker.city, "Sevilla")
        self.assertEqual(worker.address, "Reina Mercedes 11")
        self.assertEqual(worker.telephone, "666666666")
        self.assertEqual(worker.postal_code, "41013")
        self.assertEqual(worker.photo, "")
        self.assertEqual(worker.is_active, True)
        self.assertEqual(worker.is_admin, True)
        self.assertEqual(worker.ong, self.ong)

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
        worker.telephone = "654654654"
        worker.postal_code = "41004"
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
        self.assertEqual(worker.telephone, "654654654")
        self.assertEqual(worker.postal_code, "41004")
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
                                  telephone="666666666",
                                  postal_code="41015",
                                  photo="",
                                  is_active=True,
                                  is_admin=True, ong=self.ong)

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
                                  telephone="666666666",
                                  postal_code="41015",
                                  photo="",
                                  is_active=True,
                                  is_admin=True, ong=self.ong)

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
                                           telephone="666666666",
                                           postal_code="41015",
                                           photo="",
                                           is_active=True,
                                           is_admin=True, ong=self.ong)
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
                                  telephone="666666666",
                                  postal_code="41015",
                                  photo="",
                                  is_active=True,
                                  is_admin=True, ong=self.ong)

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
                                           telephone="666666666",
                                           postal_code="41015",
                                           photo="",
                                           is_active=True,
                                           is_admin=True, ong=self.ong)
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
                                           telephone="666666666",
                                           postal_code="41015",
                                           photo="",
                                           is_active=True,
                                           is_admin=True, ong=self.ong)
            worker.full_clean()

    def test_worker_create_birth_date_incorrect(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2",
                                           birth_date="bad_date",
                                           sex="Masculino",
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone="666666666",
                                           postal_code="41015",
                                           photo="",
                                           is_active=True,
                                           is_admin=True, ong=self.ong)
            worker.full_clean()

    def test_worker_create_sex_incorrect_max(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2",
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino"*50,
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone="666666666",
                                           postal_code="41015",
                                           photo="",
                                           is_active=True,
                                           is_admin=True, ong=self.ong)
            worker.full_clean()

    def test_worker_create_sex_incorrect(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2",
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="bad_sex",
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone="666666666",
                                           postal_code="41015",
                                           photo="",
                                           is_active=True,
                                           is_admin=True, ong=self.ong)
            worker.full_clean()

    def test_worker_create_city_incorrect_max(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2",
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino",
                                           city="Sevilla"*200,
                                           address="Triana 16",
                                           telephone="666666666",
                                           postal_code="41015",
                                           photo="",
                                           is_active=True,
                                           is_admin=True, ong=self.ong)
            worker.full_clean()

    def test_worker_create_address_incorrect(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2",
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino",
                                           city="Sevilla",
                                           address="Triana 16"*200,
                                           telephone="666666666",
                                           postal_code="41015",
                                           photo="",
                                           is_active=True,
                                           is_admin=True, ong=self.ong)
            worker.full_clean()

    def test_worker_create_telephone_incorrect(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2",
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino",
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone="bad_telephone",
                                           postal_code="41015",
                                           photo="",
                                           is_active=True,
                                           is_admin=True, ong=self.ong)
            worker.full_clean()

    def test_worker_create_postal_code_incorrect(self):
        with self.assertRaises(Exception):
            worker = Worker.objects.create(email="worker2@gmail.com",
                                           name="Worker2",
                                           surname="Worker2",
                                           birth_date=datetime.datetime(
                                               1998, 3, 12, tzinfo=datetime.timezone.utc),
                                           sex="Masculino",
                                           city="Sevilla",
                                           address="Triana 16",
                                           telephone="666666666",
                                           postal_code="bad_postal_code",
                                           photo="",
                                           is_active=True,
                                           is_admin=True, ong=self.ong)
            worker.full_clean()

    def test_worker_update_name_incorrect_max(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.name = "Worker"*50
            worker.full_clean()

    def test_worker_update_name_incorrect_null(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.name = None
            worker.full_clean()

    def test_worker_update_email_incorrect(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.email = "bad_email"
            worker.full_clean()

    def test_worker_update_email_incorrect_null(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.email = None
            worker.full_clean()

    def test_worker_update_surname_incorrect_max(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.surname = "Worker"*50
            worker.full_clean()

    def test_worker_update_surname_incorrect_null(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.surname = None
            worker.full_clean()

    def test_worker_update_birth_date_incorrect(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.birth_date = "bad_date"
            worker.full_clean()

    def test_worker_update_sex_incorrect_max(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.sex = "Masculino"*50
            worker.full_clean()

    def test_worker_update_sex_incorrect(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.sex = "bad_sex"
            worker.full_clean()

    def test_worker_update_city_incorrect_max(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.city = "Sevilla"*200
            worker.full_clean()

    def test_worker_update_address_incorrect(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.address = "Triana 16"*200
            worker.full_clean()

    def test_worker_update_telephone_incorrect(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.telephone = "bad_telephone"
            worker.full_clean()

    def test_worker_update_postal_code_incorrect(self):
        worker = Worker.objects.get(name="Worker2")
        with self.assertRaises(Exception):
            worker.postal_code = "bad_postal_code"
            worker.full_clean()


class UpdatePasswordTest(TestCase):

    def setUp(self):
        # Crea una ONG para los trabajadores
        self.ong = Ong.objects.create(name="Test ONG")

        # Utiliza 'unittest.mock.patch' para modificar la función 'input'
        with patch('builtins.input', side_effect=[1, 1]):
            # Crea dos trabajadores con privilegios de superusuario
            self.worker1 = Worker.objects.create_superuser(
                email='worker1@example.com', password='worker1password')

    def test_user_can_change_own_password(self):
        self.client.login(username='worker1@example.com',
                          password='worker1password')
        response = self.client.get(reverse('update_password'))
        self.assertEqual(response.status_code, 200)

        data = {
            'old_password': 'worker1password',
            'new_password1': 'new_password',
            'new_password2': 'new_password',
        }

        # Agrega el argumento `follow=True`
        response = self.client.post(
            reverse('update_password'), data, follow=True)

        # Comprueba si la URL de la respuesta es la correcta
        self.assertTrue(response.redirect_chain)
        self.assertTrue(response.redirect_chain[0][0].endswith(
            reverse('worker_list')))  # URL correcta

    def test_password_similar_to_personal_info(self):
        self.client.login(username='worker1@example.com',
                          password='worker1password')
        response = self.client.get(reverse('update_password'))
        self.assertEqual(response.status_code, 200)
        data = {
            'old_password': 'workerpassword',
            'new_password1': 'worker1@example.com',
            'new_password2': 'worker1@example.com',
        }
        response = self.client.post(
            reverse('update_password'), data, follow=True)
        self.assertContains(
            response, "La contraseña es demasiado similar a la de E-Mail.")

    def test_password_too_short(self):
        self.client.login(username='worker1@example.com',
                          password='worker1password')
        response = self.client.get(reverse('update_password'))
        self.assertEqual(response.status_code, 200)
        data = {
            'old_password': 'workerpassword',
            'new_password1': 'short',
            'new_password2': 'short',
        }
        response = self.client.post(
            reverse('update_password'), data, follow=True)
        self.assertContains(
            response, "Esta contraseña es demasiado corta. Debe contener al menos 8 caracteres.")

    def test_password_commonly_used(self):
        self.client.login(username='worker1@example.com',
                          password='worker1password')
        response = self.client.get(reverse('update_password'))
        self.assertEqual(response.status_code, 200)
        data = {
            'old_password': 'workerpassword',
            'new_password1': 'password123',
            'new_password2': 'password123',
        }
        response = self.client.post(
            reverse('update_password'), data, follow=True)
        self.assertContains(response, "Esta contraseña es demasiado común.")

    def test_password_all_numeric(self):
        self.client.login(username='worker1@example.com',
                          password='worker1password')
        response = self.client.get(reverse('update_password'))
        self.assertEqual(response.status_code, 200)
        data = {
            'old_password': 'workerpassword',
            'new_password1': '12345678',
            'new_password2': '12345678',
        }
        response = self.client.post(
            reverse('update_password'), data, follow=True)
        self.assertContains(
            response, "Esta contraseña es completamente numérica.")

    def test_password_same_as_old_password(self):
        self.client.login(username='worker1@example.com',
                          password='worker1password')
        data = {
            'old_password': 'worker1password',
            'new_password1': 'worker1password',
            'new_password2': 'worker1password',
        }
        self.client.post(reverse('update_password'), data, follow=True)

        # Comprueba si el usuario sigue autenticándose con la contraseña antigua
        self.assertTrue(self.worker1.check_password('worker1password'))
