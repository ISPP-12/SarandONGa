from datetime import datetime
from django.test import TestCase
from ong.models import Ong
from person.models import Child


class ChildTestCase(TestCase):
    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')

        self.child_update = Child.objects.create(email='test1@test.com', name='Test_1',surname='Test1 Test1', birth_date=datetime(2001,6,18),
                            sex="Femenino", city="Test1", address="Test1", telephone=123456789, postal_code=12345, photo="test1.jpg",
                            start_date=datetime(2006,2,23), termination_date=datetime(2020,9,12), expected_mission_time="2",
                            mission_house="Test1", site="Test1", subsite="Test1", father_name="Dn. Test1", father_profession="Test1",
                            mother_name="Sra. Test1", mother_profession="Test1", number_brothers_siblings=3,correspondence="Test1",ong=self.ong)
        
        Child.objects.create(email='test2@test.com', name='Test_2',surname='Test2 Test2', birth_date=datetime(2003,4,8),
                            sex="Masculino", city="Test2", address="Test2", telephone=123456789, postal_code=12345, photo="test2.jpg",
                            start_date=datetime(2008,11,12), termination_date=datetime(2021,2,1), expected_mission_time="2",
                            mission_house="Test2", site="Test2", subsite="Test2", father_name="Dn. Test2", father_profession="Test2",
                            mother_name="Sra. Test2", mother_profession="Test2", number_brothers_siblings=3,correspondence="Test2",ong=self.ong)
        
        Child.objects.create(email='test3@test.com', name='Test_3',surname='Test3 Test3', birth_date=datetime(2010,5,29),
                            sex="Femenino", city="Test3", address="Test3", telephone=123456789, postal_code=12345, photo="test3.jpg",
                            start_date=datetime(2013,11,23), termination_date=datetime(2022,9,2), expected_mission_time="2",
                            mission_house="Test3", site="Test3", subsite="Test3", father_name="Dn. Test3", father_profession="Test3",
                            mother_name="Sra. Test3", mother_profession="Test3", number_brothers_siblings=3,correspondence="Test3",ong=self.ong)
        


    def test_child_create(self):
        child = Child.objects.get(name="Test_1")
        self.assertEqual(child.email, 'test1@test.com')
        self.assertEqual(child.name, 'Test_1')
        self.assertEqual(child.surname, 'Test1 Test1')
        self.assertEqual(child.birth_date.strftime('%d/%m/%Y'),
                         datetime(2001, 6, 18).strftime('%d/%m/%Y'))
        self.assertEqual(child.sex, 'Femenino')
        self.assertEqual(child.city, 'Test1')
        self.assertEqual(child.address, 'Test1')
        self.assertEqual(child.telephone, '123456789')
        self.assertEqual(child.postal_code, '12345')
        self.assertEqual(child.photo, 'test1.jpg')
        self.assertEqual(child.start_date.strftime(
            '%d/%m/%Y'), datetime(2006, 2, 23).strftime('%d/%m/%Y'))
        self.assertEqual(child.termination_date.strftime(
            '%d/%m/%Y'), datetime(2020, 9, 12).strftime('%d/%m/%Y'))
        
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
        self.assertEqual(child2.birth_date.strftime('%d/%m/%Y'),
                         datetime(2003, 4, 8).strftime('%d/%m/%Y'))
        self.assertEqual(child2.sex, 'Masculino')
        self.assertEqual(child2.city, 'Test2')
        self.assertEqual(child2.address, 'Test2')
        self.assertEqual(child2.telephone, '123456789')
        self.assertEqual(child2.postal_code, '12345')
        self.assertEqual(child2.photo, 'test2.jpg')
        self.assertEqual(child2.start_date.strftime(
            '%d/%m/%Y'), datetime(2008, 11, 12).strftime('%d/%m/%Y'))
        self.assertEqual(child2.termination_date.strftime(
            '%d/%m/%Y'), datetime(2021, 2, 1).strftime('%d/%m/%Y'))
        
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
        self.assertEqual(child3.birth_date.strftime('%d/%m/%Y'),
                         datetime(2010, 5, 29).strftime('%d/%m/%Y'))
        self.assertEqual(child3.sex, 'Femenino')
        self.assertEqual(child3.city, 'Test3')
        self.assertEqual(child3.address, 'Test3')
        self.assertEqual(child3.telephone, '123456789')
        self.assertEqual(child3.postal_code, '12345')
        self.assertEqual(child3.photo, 'test3.jpg')
        self.assertEqual(child3.start_date.strftime(
            '%d/%m/%Y'), datetime(2013, 11, 23).strftime('%d/%m/%Y'))
        self.assertEqual(child3.termination_date.strftime(
            '%d/%m/%Y'), datetime(2022, 9, 2).strftime('%d/%m/%Y'))
        
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
        child.surname = 'newTest2 newTest2'
        child.birth_date = datetime(2004, 4, 8)
        child.sex = "Otro"
        child.city = "newTest2"
        child.address = "newTest2"
        child.telephone = 987654321
        child.postal_code = 54321
        child.photo = "newtest2.jpg"
        child.start_date = datetime(2008, 12, 12)
        child.termination_date = datetime(2021, 6, 1)
        
        child.expected_mission_time = "3"
        child.mission_house = "newTest2"
        child.site = "newTest2"
        child.subsite = "newTest2"
        child.father_name = "newDn. Test2"
        child.father_profession = "newTest2"
        child.mother_name = "newSra. Test2"
        child.mother_profession = "newTest2"
        child.number_brothers_siblings = 2
        child.correspondence = "newTest2"
        child.save()

        self.assertEqual(child.email, 'newtest2@test.com')
        self.assertEqual(child.name, 'New_Test_2')
        self.assertEqual(child.surname, 'newTest2 newTest2')
        self.assertEqual(child.birth_date.strftime('%d/%m/%Y'),
                         datetime(2004, 4, 8).strftime('%d/%m/%Y'))
        self.assertEqual(child.sex, 'Otro')
        self.assertEqual(child.city, 'newTest2')
        self.assertEqual(child.address, 'newTest2')
        self.assertEqual(child.telephone, 987654321)
        self.assertEqual(child.postal_code, 54321)
        self.assertEqual(child.photo, 'newtest2.jpg')
        self.assertEqual(child.start_date.strftime(
            '%d/%m/%Y'), datetime(2008, 12, 12).strftime('%d/%m/%Y'))
        self.assertEqual(child.termination_date.strftime(
            '%d/%m/%Y'), datetime(2021, 6, 1).strftime('%d/%m/%Y'))
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
        child = Child.objects.get(name="Test_3")
        child.delete()
        self.assertEqual(Child.objects.count(), 2)

    def test_child_incorrect_termination_date(self):
        child = Child.objects.get(name="Test_1")
        child.start_date = datetime(2015, 12, 12)
        child.termination_date = datetime(2014, 12, 12)
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_expected_mission_time(self):
        child = Child.objects.get(name="Test_1")
        child.expected_mission_time = "a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_mission_house(self):
        child = Child.objects.get(name="Test_1")
        child.mission_house = "a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_site(self):
        child = Child.objects.get(name="Test_1")
        child.site = "a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_subsite(self):
        child = Child.objects.get(name="Test_1")
        child.subsite = "a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_father_name(self):
        child = Child.objects.get(name="Test_1")
        child.father_name = "a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_father_profession(self):
        child = Child.objects.get(name="Test_1")
        child.father_profession = "a"*201
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_mother_name(self):
        child = Child.objects.get(name="Test_1")
        child.mother_name = "a"*201
        with self.assertRaises(Exception):
            child.save()


    def test_child_incorrect_number_brothers_siblings(self):
        child = Child.objects.get(name="Test_1")
        child.number_brothers_siblings = -1
        with self.assertRaises(Exception):
            child.save()

    def test_child_incorrect_correspondence(self):
        child = Child.objects.get(name="Test_1")
        child.correspondence = "a"*201
        with self.assertRaises(Exception):
            child.save()

    # TESTS UPDATE CHILD 

    def test_child_update_incorrect_name_max_lenght(self):
        child = Child.objects.get(name="Test_1")
        child.name = "a"*201
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_update_incorrect_name_null(self):
        child = Child.objects.get(name="Test_1")
        child.name = None
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_name_int(self):
        with self.assertRaises(Exception):
                self.child_update.name = 123
                self.child_update.save()
                self.child_update.full_clean()

    def test_child_update_incorrect_surname_max_lenght(self):
        child = Child.objects.get(name="Test_1")
        child.surname = "a"*201
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_update_incorrect_surname_null(self):
        child = Child.objects.get(name="Test_1")
        child.surname = None
        with self.assertRaises(Exception):
            child.save()
            self.child_update.full_clean()

    def test_child_incorrect_surname_int(self):
        with self.assertRaises(Exception):
                self.child_update.surname = 123
                self.child_update.save()
                self.child_update.full_clean()
    
    def test_child_incorrect_email(self):
        with self.assertRaises(Exception):
                self.child_update.email = "emailfalso"
                self.child_update.save()
                self.child_update.full_clean()
    
    def test_child_incorrect_birth_date(self):
            with self.assertRaises(Exception):
                self.child_update.birth_date = "23-12-23"
                self.child_update.save()
                self.child_update.full_clean()
    
    def test_child_incorrect_sex(self):
            with self.assertRaises(Exception):
                self.child_update.sex = "J"
                self.child_update.save()
                self.child_update.full_clean()
    
    def test_incorrect_city(self):
            with self.assertRaises(Exception):
                self.child_update.city = 1111
                self.child_update.save()
                self.child_update.full_clean()

    def test_incorrect_city_max_length(self):
        child = Child.objects.get(name="Test_1")
        child.city = "a"*201
        with self.assertRaises(Exception):
            child.save()
            
            
    
    def test_incorrect_addres_max_length(self):
        child = Child.objects.get(name="Test_1")
        child.address = "a"*201
        with self.assertRaises(Exception):
            child.save()
    
    def test_incorrect_telephone(self):
        child = Child.objects.get(name="Test_1")
        child.telephone = "a"*201
        with self.assertRaises(Exception):
            child.save()
    
    def test_incorrect_cellphone(self):
            with self.assertRaises(Exception):
                self.child_update.telephone = "11111111111111111111111111111111111111111111111111111111111"
                self.child_update.save()
                self.child_update.full_clean()
    
    def test_incorrect_postal_code_max_lenght(self):
        child = Child.objects.get(name="Test_1")
        child.postal_code = "a"*52
        with self.assertRaises(Exception):
            child.save()
    
    def test_incorrect_postal_code(self):
            with self.assertRaises(Exception):
                self.child_update.posta_code = "J"
                self.child_update.save()
                self.child_update.full_clean()

    def test_incorrect_expected_mission_time(self):
        child = Child.objects.get(name="Test_1")
        child.expected_mission_time = "a"*201
        with self.assertRaises(Exception):
            child.save()
    
    def test_incorrect_expected_mission_time_null(self):
        child = Child.objects.get(name="Test_1")
        child.expected_mission_time = None
        with self.assertRaises(Exception):
            child.save()
    
    def test_incorrect_start_date(self):
        child = Child.objects.get(name="Test_1")
        child.start_date = "2040-01-01"
        with self.assertRaises(Exception):
            child.save()
    
    def test_incorrect_termination_date(self):
        child = Child.objects.get(name="Test_1")
        child.termination_date = "2040-01-01"
        with self.assertRaises(Exception):
            child.save()
    

    
    def test_incorrect_mission_house_null(self):
        child = Child.objects.get(name="Test_1")
        child.mission_house = None
        with self.assertRaises(Exception):
            child.save()
    
    def test_incorrect_mission_house_max_length(self):
        child = Child.objects.get(name="Test_1")
        child.mission_house = "a"*201
        with self.assertRaises(Exception):
            child.save()
    
    def test_incorrect_site_null(self):
        child = Child.objects.get(name="Test_1")
        child.site = None
        with self.assertRaises(Exception):
            child.save()
    
    def test_incorrect_subssite_null(self):
        child = Child.objects.get(name="Test_1")
        child.subsite = None
        with self.assertRaises(Exception):
            child.save()    
    
    def test_child_incorrect_father_name_max_lenght(self):
        child = Child.objects.get(name="Test_1")
        child.father_name = "a"*201
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_father_name_null(self):
        child = Child.objects.get(name="Test_1")
        child.father_name = None
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_father_profession_max_lenght(self):
        child = Child.objects.get(name="Test_1")
        child.father_profession = "a"*201
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_father_profession_null(self):
        child = Child.objects.get(name="Test_1")
        child.father_profession = None
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_mother_name_max_lenght(self):
        child = Child.objects.get(name="Test_1")
        child.mother_name = "a"*201
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_mother_name_null(self):
        child = Child.objects.get(name="Test_1")
        child.mother_name = None
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_mother_profession_max_lenght(self):
        child = Child.objects.get(name="Test_1")
        child.mother_profession = "a"*201
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_mother_profession_null(self):
        child = Child.objects.get(name="Test_1")
        child.mother_profession = None
        with self.assertRaises(Exception):
            child.save()
    
    
    def test_child_incorrect_number_brothers_siblings_negative(self):
        child = Child.objects.get(name="Test_1")
        child.number_brothers_siblings = -1
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_correspondence_null(self):
        child = Child.objects.get(name="Test_1")
        child.correspondence = None
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_number_brothers_siblings_null(self):
        child = Child.objects.get(name="Test_1")
        child.number_brothers_siblings = None
        with self.assertRaises(Exception):
            child.save()
    
    def test_child_incorrect_ong(self):
            with self.assertRaises(Exception):
                self.subsidy.payment_date = "23-12-23"
                self.subsidy.save()
                self.child_update.full_clean()
    
    def test_child_incorrect_ong_null(self):
        child = Child.objects.get(name="Test_1")
        child.ong = None
        with self.assertRaises(Exception):
            child.save()