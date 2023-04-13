from django.test import TestCase
from ong.models import Ong
from service.models import Service, ServiceAmount
from person.models import ASEMUser
from payment.models import Payment
import datetime

class ServiceAmountTestCase(TestCase):

    def setUp(self):
        ServiceAmount.objects.create(service_type="Fisioterapia",
            user_type="SACC",
            amount=30,
            date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))

        ServiceAmount.objects.create(service_type="Logopedia",
            user_type="SACC",
            amount=30,
            date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))

    def test_service_amount_create_correct(self):
        service_amount = ServiceAmount.objects.get(service_type="Fisioterapia")
        self.assertEqual(service_amount.user_type, "SACC")
        self.assertEqual(service_amount.amount, 30)
        self.assertEqual(service_amount.date, datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))

    def test_service_amount_update_correct(self):
        service_amount = ServiceAmount.objects.get(service_type="Fisioterapia")
        self.assertEqual(service_amount.user_type, "SACC")
        self.assertEqual(service_amount.amount, 30)
        self.assertEqual(service_amount.date, datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))
        service_amount.service_type = "Neuropsicología"
        service_amount.user_type = "UCC"
        service_amount.amount = 20
        service_amount.date = datetime.datetime(2019, 1, 1, tzinfo=datetime.timezone.utc)
        service_amount.save()
        self.assertEqual(service_amount.user_type, "UCC")
        self.assertEqual(service_amount.amount, 20)
        self.assertEqual(service_amount.date, datetime.datetime(2019, 1, 1, tzinfo=datetime.timezone.utc))

    def test_service_amount_delete_correct(self):
        service_amount = ServiceAmount.objects.get(service_type="Logopedia")
        self.assertEqual(ServiceAmount.objects.count(), 2)
        service_amount.delete()
        self.assertEqual(ServiceAmount.objects.count(), 1)

    def test_service_amount_service_type_incorrect_max_length(self):
        with self.assertRaises(Exception):
            ServiceAmount.objects.create(service_type="Fisioterapiaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                user_type="SACC",
                amount=30,
                date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))

    def test_service_amount_service_type_incorrect_choices(self):
        with self.assertRaises(Exception):
            service_amount = ServiceAmount.objects.create(service_type="No es un tipo de servicio",
                user_type="SACC",
                amount=30,
                date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))
            service_amount.full_clean()

    def test_service_amount_service_type_incorrect_null(self):
        with self.assertRaises(Exception):
            ServiceAmount.objects.create(service_type=None,
                user_type="SACC",
                amount=30,
                date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))

    def test_service_amount_service_type_incorrect_blank(self):
        with self.assertRaises(Exception):
            service_amount = ServiceAmount.objects.create(service_type="",
                user_type="SACC",
                amount=30,
                date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))
            service_amount.full_clean()

    def test_service_amount_user_type_incorrect_max_length(self):
        with self.assertRaises(Exception):
            ServiceAmount.objects.create(service_type="Fisioterapia",
                user_type="SACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",
                amount=30,
                date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))

    def test_service_amount_user_type_incorrect_choices(self):
        with self.assertRaises(Exception):
            service_amount = ServiceAmount.objects.create(service_type="Fisioterapia",
                user_type="No es un tipo de usuario de ASEM",
                amount=30,
                date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))
            service_amount.full_clean()

    def test_service_amount_user_type_incorrect_null(self):
        with self.assertRaises(Exception):
            ServiceAmount.objects.create(service_type="Fisioterapia",
                user_type=None,
                amount=30,
                date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))

    def test_service_amount_amount_incorrect_type(self):
        with self.assertRaises(Exception):
            ServiceAmount.objects.create(service_type="Fisioterapia",
                user_type="SACC",
                amount="No es un número",
                date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))

    def test_service_amount_amount_incorrect_null(self):
        with self.assertRaises(Exception):
            ServiceAmount.objects.create(service_type="Fisioterapia",
                user_type="SACC",
                amount=None,
                date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))

    def test_service_date_incorrect_type(self):
        with self.assertRaises(Exception):
            ServiceAmount.objects.create(service_type="Fisioterapia",
                user_type="SACC",
                amount=30,
                date="No es una fecha")

    def test_service_date_incorrect_null(self):
        with self.assertRaises(Exception):
            ServiceAmount.objects.create(service_type="Fisioterapia",
                user_type="SACC",
                amount=30,
                date=None)

class ServiceTestCase(TestCase):

    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        self.asem_user = ASEMUser.objects.create(email="manfergom@gmail.com",
            name="Manuel",
            surname="Fernández",
            birth_date=datetime.datetime(1995, 2, 27, tzinfo=datetime.timezone.utc),
            sex="Masculino",
            city="Sevilla",
            address="Avda. Reina Mercedes, 53",
            telephone=623135837,
            postal_code=41012,
            condition="Esclerosis múltiple",
            member="Escleriosis múltiple",
            user_type="SACC",
            correspondence="Email",
            status="Soltero/a",
            family_unit_size=3,
            own_home="Vivienda propia",
            own_vehicle=False,
            bank_account_number="ES6700567834215439610225",ong=self.ong)

        self.payment_1 = Payment.objects.create(payday=datetime.datetime(2018, 2, 27, tzinfo=datetime.timezone.utc),
            amount=30, ong=self.ong)

        Payment.objects.create(payday=datetime.datetime(2018, 3, 27, tzinfo=datetime.timezone.utc),
            amount=60, ong=self.ong)

        ServiceAmount.objects.create(service_type="Fisioterapia",
            user_type="SACC",
            amount=30,
            date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))

        ServiceAmount.objects.create(service_type="Logopedia",
            user_type="SACC",
            amount=30,
            date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))
        
        Service.objects.create(service_type = "Fisioterapia",
            date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
            attendance = True,
            payment = None,
            asem_user = self.asem_user)

        Service.objects.create(service_type = "Logopedia",
            date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
            attendance = True,
            payment = None,
            asem_user = self.asem_user)

    def test_service_create_correct(self):

        service = Service.objects.get(service_type="Fisioterapia")
        self.assertEqual(service.service_type, "Fisioterapia")
        self.assertEqual(service.date, datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc))
        self.assertEqual(service.attendance, True)
        self.assertEqual(service.payment, None)
        self.assertEqual(service.asem_user, self.asem_user)

    def test_service_update_correct(self):
        service = Service.objects.get(service_type="Logopedia")
        service.service_type = "Neuropsicología"
        service.date = datetime.datetime(2019, 2, 1, tzinfo=datetime.timezone.utc)
        service.attendance = True
        service.payment = self.payment_1
        service.save()
        self.assertEqual(service.service_type, "Neuropsicología")
        self.assertEqual(service.date, datetime.datetime(2019, 2, 1, tzinfo=datetime.timezone.utc))
        self.assertEqual(service.attendance, True)
        self.assertEqual(service.payment, self.payment_1)

    def test_service_delete_correct(self):
        self.assertEqual(Service.objects.count(), 2)
        Service.objects.get(service_type="Fisioterapia").delete()
        self.assertEqual(Service.objects.count(), 1)

    def test_service_service_type_incorrect_max_length(self):
        with self.assertRaises(Exception):
            Service.objects.create(service_type = "Fisioterapiaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
                attendance = True,
                payment = None,
                asem_user = self.asem_user)

    def test_service_service_type_incorrect_choices(self):
        with self.assertRaises(Exception):
            service = Service.objects.create(service_type = "No es un tipo de servicio",
                date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
                attendance = True,
                payment = None,
                asem_user = self.asem_user)
            service.full_clean()

    def test_service_service_type_incorrect_null(self):
        with self.assertRaises(Exception):
            Service.objects.create(service_type = None,
                date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
                attendance = True,
                payment = None,
                asem_user = self.asem_user)

    def test_service_service_type_incorrect_blank(self):
        with self.assertRaises(Exception):
            service = Service.objects.create(service_type = "",
                date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
                attendance = True,
                payment = None,
                asem_user = self.asem_user)
            service.full_clean()

    def test_service_date_incorrect_type(self):
        with self.assertRaises(Exception):
            Service.objects.create(service_type = "Fisioterapia",
                date = "No es una fecha",
                attendance = True,
                payment = None,
                asem_user = self.asem_user)

    def test_service_date_incorrect_null(self):
        with self.assertRaises(Exception):
            Service.objects.create(service_type = "Fisioterapia",
                date = None,
                attendance = True,
                payment = None,
                asem_user = self.asem_user)

    def test_service_attendance_incorrect_type(self):
        with self.assertRaises(Exception):
            Service.objects.create(service_type = "Fisioterapia",
                date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
                attendance = "No es un tipo válido",
                payment = None,
                asem_user = self.asem_user)

    def test_service_attendance_incorrect_null(self):
        with self.assertRaises(Exception):
            Service.objects.create(service_type = "Fisioterapia",
                date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
                attendance = None,
                payment = None,
                asem_user = self.asem_user)

    def test_service_payment_incorrect_type(self):
        with self.assertRaises(Exception):
            Service.objects.create(service_type = "Fisioterapia",
                date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
                attendance = True,
                payment = "No es un tipo válido",
                asem_user = self.asem_user)

    def test_service_asem_user_incorrect_type(self):
        with self.assertRaises(Exception):
            Service.objects.create(service_type = "Fisioterapia",
                date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
                attendance = True,
                payment = None,
                asem_user = "No es un usuario válido")

    def test_service_asem_user_incorrect_null(self):
        with self.assertRaises(Exception):
            Service.objects.create(service_type = "Fisioterapia",
                date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
                attendance = True,
                payment = None,
                asem_user = None)
            

class UpdateServiceTestCase(TestCase):
    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        self.asem_user = ASEMUser.objects.create(email="manfergom@gmail.com",
            name="Manuel",
            surname="Fernández",
            birth_date=datetime.datetime(1995, 2, 27, tzinfo=datetime.timezone.utc),
            sex="Masculino",
            city="Sevilla",
            address="Avda. Reina Mercedes, 53",
            telephone=623135837,
            postal_code=41012,
            condition="Esclerosis múltiple",
            member="Escleriosis múltiple",
            user_type="SACC",
            correspondence="Email",
            status="Soltero/a",
            family_unit_size=3,
            own_home="Vivienda propia",
            own_vehicle=False,
            bank_account_number="ES6700567834215439610225",ong=self.ong)

        self.payment_1 = Payment.objects.create(payday=datetime.datetime(2018, 2, 27, tzinfo=datetime.timezone.utc),
            amount=30, ong=self.ong)

        Payment.objects.create(payday=datetime.datetime(2018, 3, 27, tzinfo=datetime.timezone.utc),
            amount=60, ong=self.ong)

        ServiceAmount.objects.create(service_type="Fisioterapia",
            user_type="SACC",
            amount=30,
            date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))

        ServiceAmount.objects.create(service_type="Logopedia",
            user_type="SACC",
            amount=30,
            date=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc))
        
        Service.objects.create(service_type = "Fisioterapia",
            date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
            attendance = True,
            payment = None,
            asem_user = self.asem_user)

        Service.objects.create(service_type = "Logopedia",
            date = datetime.datetime(2018, 2, 1, tzinfo=datetime.timezone.utc),
            attendance = True,
            payment = None,
            asem_user = self.asem_user)
        
    def test_update_service_correct(self):
        service = Service.objects.get(service_type="Fisioterapia")
        service.service_type = "Logopedia"
        service.date = datetime.datetime(2018, 3, 1, tzinfo=datetime.timezone.utc)
        service.attendance = False
        service.save()
        self.assertEqual(service.service_type, "Logopedia")

    def test_update_service_incorrect_service_type(self):
        service = Service.objects.get(service_type="Fisioterapia")
        with self.assertRaises(Exception):
            service.service_type = 1234
            service.clear_data()

    def test_update_service_incorrect_service_type_null(self):
        service = Service.objects.get(service_type="Fisioterapia")
        with self.assertRaises(Exception):
            service.service_type = None
            service.save()
    
    def test_update_service_incorrect_date(self):
        service = Service.objects.get(service_type="Fisioterapia")
        with self.assertRaises(Exception):
            service.date = "No es una fecha"
            service.save()

    def test_update_service_incorrect_date_null(self):
        service = Service.objects.get(service_type="Fisioterapia")
        with self.assertRaises(Exception):
            service.date = None
            service.save()

    def test_update_service_incorrect_attendance(self):
        service = Service.objects.get(service_type="Fisioterapia")
        with self.assertRaises(Exception):
            service.attendance = "No es un tipo válido"
            service.save()

    def test_update_service_incorrect_attendance_null(self):
        service = Service.objects.get(service_type="Fisioterapia")
        with self.assertRaises(Exception):
            service.attendance = None
            service.save()
    
    def test_update_service_incorrect_payment(self):
        service = Service.objects.get(service_type="Fisioterapia")
        with self.assertRaises(Exception):
            service.payment = "No es un tipo válido"
            service.save()

    def test_update_service_incorrect_asem_user(self):
        service = Service.objects.get(service_type="Fisioterapia")
        with self.assertRaises(Exception):
            service.asem_user = None
            service.save()