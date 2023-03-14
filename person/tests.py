import datetime
from django.test import TestCase
from person.models import ASEMUser,Child


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
        self.assertEqual(ASEMUser.objects.count(), 2)
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
            city="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa \
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa \
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa \
            aaaaaaaaaaaaaaaaaaaaaaaaaaaa",
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
            address="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa \
                aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa \
                aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa \
                aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
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
                
    def test_asem_user_create_own_vehicle_incorrect_null(self):
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
            
    def test_asem_user_create_bank_account_number_incorrect_pattern(self):
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
            bank_account_number='No es un patron de cuenta bancaria')
            

class ChildTestCase(TestCase):
    def setUp(self):
        Child.objects.create(email='test1@test.com', name='Test_1',surname='Test1 Test1', birth_date=datetime(2001,6,18),
                            sex="Femenino", city="Test1", address="Test1", telephone=123456789, postal_code=12345, photo="test1.jpg",
                            sponsorship_date=datetime(2006,2,23), terminatio_date=datetime(2020,9,12), study="Test1", expected_mission_time="2",
                            mission_house="Test1", site="Test1", subsite="Test1", father_name="Dn. Test1", father_profession="Test1",
                            mother_name="Sra. Test1", mother_profession="Test1", number_brothers_siblings=3,correspondence="Test1")
        
        Child.objects.create(email='test2@test.com', name='Test_2',surname='Test2 Test2', birth_date=datetime(2003,4,8),
                            sex="Masculino", city="Test2", address="Test2", telephone=123456789, postal_code=12345, photo="test2.jpg",
                            sponsorship_date=datetime(2008,11,12), terminatio_date=datetime(2021,2,1), study="Test2", expected_mission_time="2",
                            mission_house="Test2", site="Test2", subsite="Test2", father_name="Dn. Test2", father_profession="Test2",
                            mother_name="Sra. Test2", mother_profession="Test2", number_brothers_siblings=3,correspondence="Test2")
        
        Child.objects.create(email='test3@test.com', name='Test_3',surname='Test3 Test3', birth_date=datetime(2010,5,29),
                            sex="Femenino", city="Test3", address="Test3", telephone=123456789, postal_code=12345, photo="test3.jpg",
                            sponsorship_date=datetime(2013,11,23), terminatio_date=datetime(2022,9,2), study="Test3", expected_mission_time="2",
                            mission_house="Test3", site="Test3", subsite="Test3", father_name="Dn. Test3", father_profession="Test3",
                            mother_name="Sra. Test3", mother_profession="Test3", number_brothers_siblings=3,correspondence="Test3")
        
        


    def test_child_create(self):
        child = Child.objects.get(name="Test_1")
        self.assertEqual(child.email, 'test1@test.com')
        self.assertEqual(child.name, 'Test_1')
        self.assertEqual(child.surname, 'Test1 Test1')
        self.assertEqual(child.birth_date.strftime('%d/%m/%Y'), datetime(2001,6,18).strftime('%d/%m/%Y'))
        self.assertEqual(child.sex, 'Femenino')
        self.assertEqual(child.city, 'Test1')
        self.assertEqual(child.address, 'Test1')
        self.assertEqual(child.telephone, 123456789)
        self.assertEqual(child.postal_code, 12345)
        self.assertEqual(child.photo, 'test1.jpg')
        self.assertEqual(child.sponsorship_date.strftime('%d/%m/%Y'), datetime(2006,2,23).strftime('%d/%m/%Y'))
        self.assertEqual(child.terminatio_date.strftime('%d/%m/%Y'), datetime(2020,9,12).strftime('%d/%m/%Y'))
        self.assertEqual(child.study, 'Test1')
        self.assertEqual(child.expected_mission_time, '2')
        self.assertEqual(child.mission_house, 'Test1')
        self.assertEqual(child.site, 'Test1')
        self.assertEqual(child.subsite, 'Test1')
        self.assertEqual(child.father_name, 'Dn. Test1')
        self.assertEqual(child.father_profession, 'Test1')
        self.assertEqual(child.mother_name, 'Sra. Test1')
        self.assertEqual(child.mother_profession, 'Test1')
        self.assertEqual(child.number_brothers_siblings, 3)
        self.assertEqual(child.correspondence, 'Test1')

        child2 = Child.objects.get(name="Test_2")
        self.assertEqual(child2.email, 'test2@test.com')
        self.assertEqual(child2.name, 'Test_2')
        self.assertEqual(child2.surname, 'Test2 Test2')
        self.assertEqual(child2.birth_date.strftime('%d/%m/%Y'), datetime(2003,4,8).strftime('%d/%m/%Y'))
        self.assertEqual(child2.sex, 'Masculino')
        self.assertEqual(child2.city, 'Test2')
        self.assertEqual(child2.address, 'Test2')
        self.assertEqual(child2.telephone, 123456789)
        self.assertEqual(child2.postal_code, 12345)
        self.assertEqual(child2.photo, 'test2.jpg')
        self.assertEqual(child2.sponsorship_date.strftime('%d/%m/%Y'), datetime(2008,11,12).strftime('%d/%m/%Y'))
        self.assertEqual(child2.terminatio_date.strftime('%d/%m/%Y'), datetime(2021,2,1).strftime('%d/%m/%Y'))
        self.assertEqual(child2.study, 'Test2')
        self.assertEqual(child2.expected_mission_time, '2')
        self.assertEqual(child2.mission_house, 'Test2')
        self.assertEqual(child2.site, 'Test2')
        self.assertEqual(child2.subsite, 'Test2')
        self.assertEqual(child2.father_name, 'Dn. Test2')
        self.assertEqual(child2.father_profession, 'Test2')
        self.assertEqual(child2.mother_name, 'Sra. Test2')
        self.assertEqual(child2.mother_profession, 'Test2')
        self.assertEqual(child2.number_brothers_siblings, 3)
        self.assertEqual(child2.correspondence, 'Test2')

        child3 = Child.objects.get(name="Test_3")
        self.assertEqual(child3.email, 'test3@test.com')
        self.assertEqual(child3.name, 'Test_3')
        self.assertEqual(child3.surname, 'Test3 Test3')
        self.assertEqual(child3.birth_date.strftime('%d/%m/%Y'), datetime(2010,5,29).strftime('%d/%m/%Y'))
        self.assertEqual(child3.sex, 'Femenino')
        self.assertEqual(child3.city, 'Test3')
        self.assertEqual(child3.address, 'Test3')
        self.assertEqual(child3.telephone, 123456789)
        self.assertEqual(child3.postal_code, 12345)
        self.assertEqual(child3.photo, 'test3.jpg')
        self.assertEqual(child3.sponsorship_date.strftime('%d/%m/%Y'), datetime(2013,11,23).strftime('%d/%m/%Y'))
        self.assertEqual(child3.terminatio_date.strftime('%d/%m/%Y'), datetime(2022,9,2).strftime('%d/%m/%Y'))
        self.assertEqual(child3.study, 'Test3')
        self.assertEqual(child3.expected_mission_time, '2')
        self.assertEqual(child3.mission_house, 'Test3')
        self.assertEqual(child3.site, 'Test3')
        self.assertEqual(child3.subsite, 'Test3')
        self.assertEqual(child3.father_name, 'Dn. Test3')
        self.assertEqual(child3.father_profession, 'Test3')
        self.assertEqual(child3.mother_name, 'Sra. Test3')
        self.assertEqual(child3.mother_profession, 'Test3')
        self.assertEqual(child3.number_brothers_siblings, 3)
        self.assertEqual(child3.correspondence, 'Test3')

    def test_child_update(self):
        child = Child.objects.get(name="Test_2")
        child.email = "newtest2@test.com"
        child.name = "New_Test_2"
        child.surname='newTest2 newTest2'
        child.birth_date=datetime(2004,4,8)
        child.sex="Otro"
        child.city="newTest2"
        child.address="newTest2"
        child.telephone=987654321
        child.postal_code=54321
        child.photo="newtest2.jpg"
        child.sponsorship_date=datetime(2008,12,12)
        child.terminatio_date=datetime(2021,6,1)
        child.study="newTest2"
        child.expected_mission_time="3"
        child.mission_house="newTest2"
        child.site="newTest2"
        child.subsite="newTest2"
        child.father_name="newDn. Test2"
        child.father_profession="newTest2"
        child.mother_name="newSra. Test2"
        child.mother_profession="newTest2"
        child.number_brothers_siblings=2
        child.correspondence="newTest2"
        child.save()

        self.assertEqual(child.email, 'newtest2@test.com')
        self.assertEqual(child.name, 'New_Test_2')
        self.assertEqual(child.surname, 'newTest2 newTest2')
        self.assertEqual(child.birth_date.strftime('%d/%m/%Y'), datetime(2004,4,8).strftime('%d/%m/%Y'))
        self.assertEqual(child.sex, 'Otro')
        self.assertEqual(child.city, 'newTest2')
        self.assertEqual(child.address, 'newTest2')
        self.assertEqual(child.telephone, 987654321)
        self.assertEqual(child.postal_code, 54321)
        self.assertEqual(child.photo, 'newtest2.jpg')
        self.assertEqual(child.sponsorship_date.strftime('%d/%m/%Y'), datetime(2008,12,12).strftime('%d/%m/%Y'))
        self.assertEqual(child.terminatio_date.strftime('%d/%m/%Y'), datetime(2021,6,1).strftime('%d/%m/%Y'))
        self.assertEqual(child.study, 'newTest2')
        self.assertEqual(child.expected_mission_time, '3')
        self.assertEqual(child.mission_house, 'newTest2')
        self.assertEqual(child.site, 'newTest2')
        self.assertEqual(child.subsite, 'newTest2')
        self.assertEqual(child.father_name, 'newDn. Test2')
        self.assertEqual(child.father_profession, 'newTest2')
        self.assertEqual(child.mother_name, 'newSra. Test2')
        self.assertEqual(child.mother_profession, 'newTest2')
        self.assertEqual(child.number_brothers_siblings, 2)
        self.assertEqual(child.correspondence, 'newTest2')


    def test_child_delete(self):
        child= Child.objects.get(name="Test_3")
        child.delete()
        self.assertEqual(Child.objects.count(), 2)

    def test_child_incorrect_terminatio_date(self):
        child = Child.objects.get(name="Test_1")
        child.sponsorship_date=datetime(2015,12,12)
        child.terminatio_date =datetime(2014,12,12)
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_study(self):
        child = Child.objects.get(name="Test_1")
        child.study="a"*201
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_expected_mission_time(self):
        child = Child.objects.get(name="Test_1")
        child.expected_mission_time="a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_mission_house(self):
        child = Child.objects.get(name="Test_1")
        child.mission_house="a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_site(self):
        child = Child.objects.get(name="Test_1")
        child.site="a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_subsite(self):
        child = Child.objects.get(name="Test_1")
        child.subsite="a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_father_name(self):
        child = Child.objects.get(name="Test_1")
        child.father_name="a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_father_profession(self):
        child = Child.objects.get(name="Test_1")
        child.father_profession="a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_mother_name(self):
        child = Child.objects.get(name="Test_1")
        child.mother_name="a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_mother_profession(self):
        child = Child.objects.get(name="Test_1")
        child.mother_profession="a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_number_brothers_siblings(self):
        child = Child.objects.get(name="Test_1")
        child.number_brothers_siblings= -1
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_correspondence(self):
        child = Child.objects.get(name="Test_1")
        child.correspondence="a"*201
        with self.assertRaises(Exception):
            child.save()
