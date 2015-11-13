from django.test import TestCase
from contacts.models import Person


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name="John", last_name="Doe")
        Person.objects.create(first_name="Jane", middle_name="Patterson", last_name="Doe")
        Person.objects.create(first_name="Mark")

    def test_person_all_fields(self):
        jane = Person.objects.get(first_name="Jane")
        self.assertIsNotNone(jane.first_name)
        self.assertIsNotNone(jane.last_name)
        self.assertIsNotNone(jane.middle_name)

    def test_person_first_name_only(self):
        mark = Person.obects.get(first_name="Mark")
        self.assertIsNone(mark.last_name)
        self.assertIsNone(mark.middle_name)
