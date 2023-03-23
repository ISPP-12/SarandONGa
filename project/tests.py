import datetime
from django.test import TestCase
from ong.models import Ong
from .models import Project


class ProjectTestCase(TestCase):

    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        self.ong2 = Ong.objects.create(name='Mi ONG2')
        self.project_update = Project.objects.create(title="Título",
                                                     country="Españita",
                                                     start_date=datetime.date(
                                                         2023, 1, 3),
                                                     end_date=datetime.date(
                                                         2024, 1, 3),
                                                     number_of_beneficiaries=3,
                                                     amount=15000,
                                                     announcement_date=datetime.date(
                                                         2024, 1, 3),
                                                     ong=self.ong)

    def test_project_create(self):
        project = Project.objects.get(title="Título")
        self.assertEqual(project.title, "Título")
        self.assertEqual(project.country, "Españita")
        self.assertEqual(project.number_of_beneficiaries, 3)
        self.assertEqual(project.amount, 15000)

    def test_project_delete(self):
        project = Project.objects.get(title="Título")
        self.assertEqual(Project.objects.count(), 1)
        project.delete()
        self.assertEqual(Project.objects.count(), 0)

    def test_project_update(self):
        self.project_update.title = "Update"
        self.project_update.country = "Change"
        self.project_update.start_date = datetime.datetime(
            2003, 6, 14, tzinfo=datetime.timezone.utc)
        self.project_update.end_date = datetime.datetime(
            2003, 6, 14, tzinfo=datetime.timezone.utc)
        self.project_update.number_of_beneficiaries = 7
        self.project_update.amount = 12
        self.project_update.announcement_date = datetime.datetime(
            2003, 7, 14, tzinfo=datetime.timezone.utc)
        self.project_update.ong = self.ong2
        self.project_update.save()
        self.assertEqual(self.project_update.title, "Update")
        self.assertEqual(self.project_update.country, "Change")
        self.assertEqual(self.project_update.start_date, datetime.datetime(
            2003, 6, 14, tzinfo=datetime.timezone.utc))
        self.assertEqual(self.project_update.end_date, datetime.datetime(
            2003, 6, 14, tzinfo=datetime.timezone.utc))
        self.assertEqual(self.project_update.number_of_beneficiaries, 7)
        self.assertEqual(self.project_update.amount, 12)
        self.assertEqual(self.project_update.announcement_date, datetime.datetime(
            2003, 7, 14, tzinfo=datetime.timezone.utc))
        self.assertEqual(self.project_update.ong, self.ong2)

    ### TESTS UPDATE PROJECT ###

    def test_project_update_title_incorrect_max_length(self):
        with self.assertRaises(Exception):
            self.project_update.title = "T" * 101
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_title_incorrect_null(self):
        with self.assertRaises(Exception):
            self.project_update.title = None
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_title_incorrect_blank(self):
        with self.assertRaises(Exception):
            self.project_update.title = ""
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_country_incorrect_max_length(self):
        with self.assertRaises(Exception):
            self.project_update.country = "C" * 101
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_start_date_incorrect(self):
        with self.assertRaises(Exception):
            self.project_update.start_date = "incorrectDate"
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_end_date_incorrect(self):
        with self.assertRaises(Exception):
            self.project_update.end_date = "incorrectDate"
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_end_date_before_start_date(self):
        with self.assertRaises(Exception):
            self.project_update.start_date = datetime.datetime(
                2003, 7, 14, tzinfo=datetime.timezone.utc)
            self.project_update.end_date = datetime.datetime(
                1990, 7, 14, tzinfo=datetime.timezone.utc)
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_number_of_beneficiaries_incorrect(self):
        with self.assertRaises(Exception):
            self.project_update.number_of_beneficiaries = "incorrectNumber"
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_number_of_beneficiaries_incorrect_min(self):
        with self.assertRaises(Exception):
            self.project_update.number_of_beneficiaries = -1
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_amount_incorrect(self):
        with self.assertRaises(Exception):
            self.project_update.amount = "incorrectNumber"
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_amount_incorrect_min(self):
        with self.assertRaises(Exception):
            self.project_update.amount = -1
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_announcement_date_incorrect(self):
        with self.assertRaises(Exception):
            self.project_update.announcement_date = "incorrectDate"
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_ong_incorrect(self):
        with self.assertRaises(Exception):
            self.project_update.ong = "incorrectOng"
            self.project_update.full_clean()
            self.project_update.save()

    def test_project_update_ong_incorrect_null(self):
        with self.assertRaises(Exception):
            self.project_update.ong = None
            self.project_update.full_clean()
            self.project_update.save()
