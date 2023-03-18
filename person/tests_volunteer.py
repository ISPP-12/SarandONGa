from django.test import TestCase
from .models import Volunteer
from datetime import date

class VolunteerTestCase(TestCase):
    def setUp(self):
        Volunteer.objects.create(
            name = 'John',
            surname = 'Smith',
            email = 'johnsmith@gmail.com',
            dni = '12345678Z',
            job = 'Developer',
            dedication_time = 10,
            contract_start_date = date(2023, 1, 20),
            contract_end_date = date(2023, 2, 5),
            raffle = False,
            lottery = False,
            is_member = False,
            pres_table = False,
            is_contributor = False,
            notes = 'This is a note',
            entity = 'Entity',
            table = 'Table',
            volunteer_type = 'Otro'
        )

        Volunteer.objects.create(
            name = 'Gabriel',
            surname = 'Moreno',
            email = 'gabrimoreno@gmail.com',
            dni = '23456781Z',
            job = 'Developer',
            dedication_time = 10,
            contract_start_date = date(2023, 1, 20),
            contract_end_date = date(2023, 2, 5),
            raffle = False,
            lottery = False,
            is_member = False,
            pres_table = False,
            is_contributor = False,
            notes = 'This is a note',
            entity = 'Entity',
            table = 'Table',
            volunteer_type = 'Otro'
        )
            
    def test_volunteer_correct_creation(self):

        volunteer1 = Volunteer.objects.get(name='John')
        volunteer2 = Volunteer.objects.get(name='Gabriel')

        self.assertEqual(volunteer1.name, 'John')
        self.assertEqual(volunteer1.surname, 'Smith')
        self.assertEqual(volunteer1.email, 'johnsmith@gmail.com')
        self.assertEqual(volunteer1.dni, '12345678Z')
        self.assertEqual(volunteer1.job, 'Developer')
        self.assertEqual(volunteer1.dedication_time, 10)
        self.assertEqual(volunteer1.contract_start_date, date(2023, 1, 20))
        self.assertEqual(volunteer1.contract_end_date, date(2023, 2, 5))
        self.assertEqual(volunteer1.raffle, False)
        self.assertEqual(volunteer1.lottery, False)
        self.assertEqual(volunteer1.is_member, False)
        self.assertEqual(volunteer1.pres_table, False)
        self.assertEqual(volunteer1.is_contributor, False)
        self.assertEqual(volunteer1.notes, 'This is a note')
        self.assertEqual(volunteer1.entity, 'Entity')
        self.assertEqual(volunteer1.table, 'Table')
        self.assertEqual(volunteer1.volunteer_type, 'Otro')

        self.assertEqual(volunteer2.name, 'Gabriel')
        self.assertEqual(volunteer2.surname, 'Moreno')
        self.assertEqual(volunteer2.email, 'gabrimoreno@gmail.com')
        self.assertEqual(volunteer2.dni, '23456781Z')
        self.assertEqual(volunteer2.job, 'Developer')
        self.assertEqual(volunteer2.dedication_time, 10)
        self.assertEqual(volunteer2.contract_start_date, date(2023, 1, 20))
        self.assertEqual(volunteer2.contract_end_date, date(2023, 2, 5))
        self.assertEqual(volunteer2.raffle, False)
        self.assertEqual(volunteer2.lottery, False)
        self.assertEqual(volunteer2.is_member, False)
        self.assertEqual(volunteer2.pres_table, False)
        self.assertEqual(volunteer2.is_contributor, False)
        self.assertEqual(volunteer2.notes, 'This is a note')
        self.assertEqual(volunteer2.entity, 'Entity')
        self.assertEqual(volunteer2.table, 'Table')
        self.assertEqual(volunteer2.volunteer_type, 'Otro')

    def test_volunteer_correct_update(self):

        volunteer2 = Volunteer.objects.get(name='Gabriel')

        self.assertEqual(volunteer2.name, 'Gabriel')
        self.assertEqual(volunteer2.surname, 'Moreno')
        self.assertEqual(volunteer2.email, 'gabrimoreno@gmail.com')
        self.assertEqual(volunteer2.dni, '23456781Z')
        self.assertEqual(volunteer2.job, 'Developer')
        self.assertEqual(volunteer2.dedication_time, 10)
        self.assertEqual(volunteer2.contract_start_date, date(2023, 1, 20))
        self.assertEqual(volunteer2.contract_end_date, date(2023, 2, 5))
        self.assertEqual(volunteer2.raffle, False)
        self.assertEqual(volunteer2.lottery, False)
        self.assertEqual(volunteer2.is_member, False)
        self.assertEqual(volunteer2.pres_table, False)
        self.assertEqual(volunteer2.is_contributor, False)
        self.assertEqual(volunteer2.notes, 'This is a note')
        self.assertEqual(volunteer2.entity, 'Entity')
        self.assertEqual(volunteer2.table, 'Table')
        self.assertEqual(volunteer2.volunteer_type, 'Otro')

        volunteer2.name = 'Gabriel Update'
        volunteer2.surname = 'Moreno Update'
        volunteer2.email = 'gabrimorenoupdate@gmail.com'
        volunteer2.dni = '34567812Z'
        volunteer2.job = 'Developer Update'
        volunteer2.dedication_time = 20
        volunteer2.contract_start_date = date(2023, 1, 15)
        volunteer2.contract_end_date = date(2023, 2, 1)
        volunteer2.raffle = True
        volunteer2.lottery = True
        volunteer2.is_member = True
        volunteer2.pres_table = True
        volunteer2.is_contributor = True
        volunteer2.notes = 'This is a note update'
        volunteer2.entity = 'Entity Update'
        volunteer2.table = 'Table Update'
        volunteer2.volunteer_type = 'Alumno en prácticas'

        volunteer2.save()

        self.assertEqual(volunteer2.name, 'Gabriel Update')
        self.assertEqual(volunteer2.surname, 'Moreno Update')
        self.assertEqual(volunteer2.email, 'gabrimorenoupdate@gmail.com')
        self.assertEqual(volunteer2.dni, '34567812Z')
        self.assertEqual(volunteer2.job, 'Developer Update')
        self.assertEqual(volunteer2.dedication_time, 20)
        self.assertEqual(volunteer2.contract_start_date, date(2023, 1, 15))
        self.assertEqual(volunteer2.contract_end_date, date(2023, 2, 1))
        self.assertEqual(volunteer2.raffle, True)
        self.assertEqual(volunteer2.lottery, True)
        self.assertEqual(volunteer2.is_member, True)
        self.assertEqual(volunteer2.pres_table, True)
        self.assertEqual(volunteer2.is_contributor, True)
        self.assertEqual(volunteer2.notes, 'This is a note update')
        self.assertEqual(volunteer2.entity, 'Entity Update')
        self.assertEqual(volunteer2.table, 'Table Update')
        self.assertEqual(volunteer2.volunteer_type, 'Alumno en prácticas')

    def test_volunteer_correct_delete(self):

        self.assertEqual(Volunteer.objects.count(), 2)

        volunteer2 = Volunteer.objects.get(name='Gabriel')
        volunteer2.delete()

        self.assertEqual(Volunteer.objects.count(), 1)


    def test_volunteer_dni_incorrect_unique(self):
        with self.assertRaises(Exception):
            Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '12345678Z',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_dni_incorrect_max_length(self):
        with self.assertRaises(Exception):
            Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '123456789Z',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_dni_incorrect_format(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '1234567AA',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )
            volunteer.full_clean()

    def test_volunteer_dni_incorrect_blank(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )
            volunteer.full_clean()

    def test_volunteer_dni_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = None,
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_job_incorrect_max_length(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'D'*51,
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_job_incorrect_blank(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = '',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )
            volunteer.full_clean()

    def test_volunteer_job_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = None,
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_dedication_time_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = None,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_dedication_time_incorrect_value(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail-com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = "Valor inválido",
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_contract_start_date_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = None,
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_contract_start_date_incorrect_value(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = "Valor inválido",
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_contract_end_date_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = None,
                raffle = False, 
                lottery = False,
                is_member = False,  
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_contract_end_date_incorrect_value(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = "Valor inválido",
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_contract_end_date_incorrect_date(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2022, 1, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )
            volunteer.full_clean()
            

    def test_volunteer_raffle_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = None,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_raffle_incorrect_value(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = "Valor inválido",
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_lottery_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = None,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_lottery_incorrect_value(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = "Valor inválido",
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_is_member_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = None,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_is_member_incorrect_value(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = "Valor inválido",
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_pres_table_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = None,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_pres_table_incorrect_value(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = "Valor inválido",
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_is_contributor_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = None,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_is_contributor_incorrect_value(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = "Valor inválido",
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_notes_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = None,
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_entity_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = None,
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_entity_incorrect_max_length(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'E' * 51,
                table = 'Table',
                volunteer_type = 'Otro'
            )

    def test_volunteer_table_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = None,
                volunteer_type = 'Otro'
            )

    def test_volunteer_table_incorrect_max_length(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'T' * 51,
                volunteer_type = 'Otro'
            )

    def test_volunteer_volunteer_type_incorrect_max_length(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'T' * 21
            )

    def test_volunteer_volunteer_type_incorrect_null(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = None
            )

    def test_volunteer_volunteer_type_incorrect_blank(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = ''
            )
            volunteer.full_clean()

    def test_volunteer_volunteer_type_incorrect_value(self):
        with self.assertRaises(Exception):
            volunteer = Volunteer.objects.create(
                name = 'Jesús',
                surname = 'García',
                email = 'jgarcia@gmail.com',
                dni = '22345678A',  
                job = 'Developer',
                dedication_time = 10,
                contract_start_date = date(2023, 1, 20),
                contract_end_date = date(2023, 2, 5),
                raffle = False,
                lottery = False,
                is_member = False,
                pres_table = False,
                is_contributor = False,
                notes = 'This is a note',
                entity = 'Entity',
                table = 'Table',
                volunteer_type = 'Volunteer'
            )
            volunteer.full_clean()
