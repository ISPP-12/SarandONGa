import datetime
from xml.dom import ValidationErr
from django.test import TestCase
from person.models import ASEMUser


class ASEMUserTestCase(TestCase):

    def setUp(self):
       ASEMUser.objects.create(email="tcamerob@gmail.com",
        name="Tomas",
        surname="Camero",
        birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
        sex="Masculino",
        city="Sevilla",
        address="Logroño 19",
        telephone=691644398,
        postal_code=41730,condition="Esclerosis múltiple",
        member="Escleriosis múltiple",
        user_type="SACC",
        correspondence="Email",
        status="Casado/a",
        family_unit_size=4,
        own_home="Vivienda compartida",
        own_vehicle=True,
        bank_account_number="ES6700832134418939683447")
       
       ASEMUser.objects.create(email="tcamerob2@gmail.com",
        name="Tomas2",
        surname="Camero2",
        birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
        sex="Femenino",
        city="Sevilla",
        address="Logroño 20",
        telephone=691644398,
        postal_code=41730,
        condition="ICTUS",
        member="ELA",
        user_type="OTROS",
        correspondence="CC",
        status="F",
        family_unit_size=0,
        own_home="VP",
        own_vehicle=False,
        bank_account_number="ES6700832134418939683449")
       
    def test_asem_user_create(self):
        asemuser = ASEMUser.objects.get(name="Tomas")
        self.assertEqual(asemuser.name, "Tomas")
        self.assertEqual(asemuser.surname, "Camero")
        self.assertEqual(asemuser.birth_date.strftime('%Y-%m-%d'), "2000-01-24")

    def test_asem_user_delete(self):
        asemuser = ASEMUser.objects.get(name="Tomas")
        asemuser.delete()
        self.assertEqual(ASEMUser.objects.count(), 1)
        
    def test_asem_user_update(self):
        asemuser = ASEMUser.objects.get(name="Tomas2")
        asemuser.name = "Tomasito"
        asemuser.surname="Camerin"
        asemuser.sex="Femenino"
        asemuser.city="Cadiz"
        asemuser.address="Logroño 21"
        asemuser.birth_date=datetime.datetime(2001, 1, 24, tzinfo=datetime.timezone.utc)
        asemuser.telephone=691644399
        asemuser.postal_code=41731
        asemuser.condition="OTROS"
        asemuser.member="UNA"
        asemuser.user_type="UCC"
        asemuser.correspondence="SR"
        asemuser.status="D"
        asemuser.family_unit_size=2
        asemuser.own_home="VC"
        asemuser.own_vehicle=True
        asemuser.bank_account_number="ES6700832134418939683447"
        asemuser.save()
        self.assertEqual(asemuser.name, "Tomasito")
        self.assertEqual(asemuser.surname,"Camerin")
        self.assertEqual(asemuser.birth_date.strftime('%Y-%m-%d'), "2001-01-24")
        self.assertEqual(asemuser.sex,"Femenino")
        self.assertEqual(asemuser.city,"Cadiz")
        self.assertEqual(asemuser.address,"Logroño 21")
        self.assertEqual(asemuser.telephone,691644399)
        self.assertEqual(asemuser.postal_code,41731)
        self.assertEqual(asemuser.condition,"OTROS")
        self.assertEqual(asemuser.member,"UNA")
        self.assertEqual(asemuser.user_type,"UCC")
        self.assertEqual(asemuser.correspondence,"SR")
        self.assertEqual(asemuser.status,"D")
        self.assertEqual(asemuser.family_unit_size,2)
        self.assertEqual(asemuser.own_home,"VC")
        self.assertEqual(asemuser.own_vehicle,True)
        self.assertEqual(asemuser.bank_account_number,"ES6700832134418939683447")
        
    def test_asem_user_create_name_incorrect_max(self):
        with self.assertRaises(Exception):
            ASEMUser.objects.create(email="tcamerob3@gmail.com",
            name="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            surname="Camero3",
            birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
            sex="Femenino",
            city="Sevilla",
            telephone=691644398,
            postal_code=41730,
            condition="ICTUS",
            member="ELA",
            user_type="OTROS",
            correspondence="CC",
            status="F",
            family_unit_size=0,
            own_home="VP",
            own_vehicle=False,
            bank_account_number="ES6700832134418939683449")
    
    def test_asem_user_create_name_incorrect_null(self):
        with self.assertRaises(Exception):
            ASEMUser.objects.create(email="tcamerob3@gmail.com",
            name=None,
            surname="Camero3",
            birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
            sex="Femenino",
            city="Sevilla",
            telephone=691644398,
            postal_code=41730,
            condition="ICTUS",
            member="ELA",
            user_type="OTROS",
            correspondence="CC",
            status="F",
            family_unit_size=0,
            own_home="VP",
            own_vehicle=False,
            bank_account_number="ES6700832134418939683449")
            
    def test_asem_user_create_email_incorrect(self):
        with self.assertRaises(Exception):
            user = ASEMUser.objects.create(email="No es un email",
            name="Tomas",
            surname="Camero3",
            birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
            sex="Femenino",
            city="Sevilla",
            telephone=691644398,
            postal_code=41730,
            condition="ICTUS",
            member="ELA",
            user_type="OTROS",
            correspondence="CC",
            status="F",
            family_unit_size=0,
            own_home="VP",
            own_vehicle=False,
            bank_account_number="ES6700832134418939683449")
            user.full_clean()
            
    def test_asem_user_create_email_incorrect_null(self):
        with self.assertRaises(Exception):
            ASEMUser.objects.create(email = None,
            name="Tomas",
            surname="Camero3",
            birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
            sex="Femenino",
            city="Sevilla",
            telephone=691644398,
            postal_code=41730,
            condition="ICTUS",
            member="ELA",
            user_type="OTROS",
            correspondence="CC",
            status="F",
            family_unit_size=0,
            own_home="VP",
            own_vehicle=False,
            bank_account_number="ES6700832134418939683449")
            
    def test_asem_user_create_surname_incorrect_null(self):
        with self.assertRaises(Exception):
            user = ASEMUser.objects.create(email="tcamerob2@gmail.com",
            name="Tomas2",
            surname=None,
            birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
            sex="Femenino",
            city="Sevilla",
            telephone=691644398,
            postal_code=41730,
            condition="ICTUS",
            member="ELA",
            user_type="OTROS",
            correspondence="CC",
            status="F",
            family_unit_size=0,
            own_home="VP",
            own_vehicle=False,
            bank_account_number="ES6700832134418939683449")
            user.full_clean()
            
    def test_asem_user_create_surname_incorrect_max(self):
        with self.assertRaises(Exception):
            user = ASEMUser.objects.create(email="tcamerob2@gmail.com",
            name="Tomas2",
            surname='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
            birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
            sex="Femenino",
            city="Sevilla",
            telephone=691644398,
            postal_code=41730,
            condition="ICTUS",
            member="ELA",
            user_type="OTROS",
            correspondence="CC",
            status="F",
            family_unit_size=0,
            own_home="VP",
            own_vehicle=False,
            bank_account_number="ES6700832134418939683449")
            user.full_clean()
            
    def test_asem_user_create_birth_date_incorrect(self):
        with self.assertRaises(Exception):
            user = ASEMUser.objects.create(email="tcamerob2@gmail.com",
            name="Tomas2",
            surname='Camero',
            birth_date="No es una fecha",
            sex="Femenino",
            city="Sevilla",
            telephone=691644398,
            postal_code=41730,
            condition="ICTUS",
            member="ELA",
            user_type="OTROS",
            correspondence="CC",
            status="F",
            family_unit_size=0,
            own_home="VP",
            own_vehicle=False,
            bank_account_number="ES6700832134418939683449")
            user.full_clean()

    def test_asem_user_create_sex_incorrect_max(self):
            with self.assertRaises(Exception):
                user = ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                city="Sevilla",
                telephone=691644398,
                postal_code=41730,
                condition="ICTUS",
                member="ELA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                user.full_clean()
                
    def test_asem_user_create_sex_incorrect(self):
            with self.assertRaises(Exception):
                user = ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="No es un sex",
                city="Sevilla",
                telephone=691644398,
                postal_code=41730,
                condition="ICTUS",
                member="ELA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                user.full_clean()
                
    def test_asem_user_create_city_incorrect_max(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                telephone=691644398,
                postal_code=41730,
                condition="ICTUS",
                member="ELA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_address_incorrect(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                telephone=691644398,
                postal_code=41730,
                condition="ICTUS",
                member="ELA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_telephone_incorrect(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone="No es un telefono",
                postal_code=41730,
                condition="ICTUS",
                member="ELA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_postal_code_incorrect(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code="No es un código postal",
                condition="ICTUS",
                member="ELA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_condition_incorrect_max(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                member="ELA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_condition_incorrect(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="No es una condición",
                member="ELA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_condition_incorrect_null(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition=None,
                member="ELA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
    
    def test_asem_user_create_member_incorrect_max(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_member_incorrect(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="No es una membresia",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
    
    def test_asem_user_create_member_incorrect_null(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member=None,
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_user_type_incorrect_max(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_user_type_incorrect(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="No es un tipo de User",
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_user_type_incorrect_null(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type=None,
                correspondence="CC",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_correspondence_incorrect_max(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
    
    def test_asem_user_create_correspondence_incorrect(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="No es un tipo de correspondencia",
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_correspondence_incorrect_null(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence=None,
                status="F",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_status_incorrect_max(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_status_incorrect(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status="No es un estado",
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_status_incorrect_null(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status=None,
                family_unit_size=0,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_family_incorrect_min(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=-1,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_family_incorrect_max(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=31,
                own_home="VP",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_own_home_incorrect_max(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=1,
                own_home="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_own_home_incorrect(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=1,
                own_home="No es un tipo",
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_own_home_incorrect_null(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=1,
                own_home=None,
                own_vehicle=False,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_own_vehicle_incorrect(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=1,
                own_home="VP",
                own_vehicle="No es un booleano",
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_own_vehicle_incorrect(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=1,
                own_home="VP",
                own_vehicle=None,
                bank_account_number="ES6700832134418939683449")
                
    def test_asem_user_create_bank_account_number_incorrect_max(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=1,
                own_home="VP",
                own_vehicle=True,
                bank_account_number="ES11111111111111111111111")
    
    def test_asem_user_create_bank_account_number_incorrect_null(self):
            with self.assertRaises(Exception):
                ASEMUser.objects.create(email="tcamerob2@gmail.com",
                name="Tomas2",
                surname='Camero',
                birth_date=datetime.datetime(2000, 1, 24, tzinfo=datetime.timezone.utc),
                sex="M",
                city="Sevilla",
                address="Logroño 19",
                telephone=691644398,
                postal_code=41730,
                condition="EM",
                member="UNA",
                user_type="OTROS",
                correspondence="CC",
                status="F",
                family_unit_size=1,
                own_home="VP",
                own_vehicle=True,
                bank_account_number=None)
                
    
                