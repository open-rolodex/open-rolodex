from django.test import TestCase
from contacts.models import Person


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name="John", last_name="Doe")
        Person.objects.create(first_name="Jane", middle_name="Patterson", last_name="Doe")
        Person.objects.create(first_name="Mark")

    def test_person_all_fields(self):
        jane = Person.objects.get(first_name="Jane")
        self.assertIsNot(jane.first_name, u'')
        self.assertIsNot(jane.last_name, u'')
        self.assertIsNot(jane.middle_name, u'')

    def test_person_first_name_only(self):
        mark = Person.objects.get(first_name="Mark")
        self.assertIsNot(mark.first_name, u'')
        self.assertIs(mark.last_name, u'')
        self.assertIs(mark.middle_name, u'')

    def test_person_no_last_name(self):
        john = Person.objects.get(first_name="John")
        self.assertIs(john.middle_name, u'')
        self.assertIsNot(john.first_name, u'')
        self.assertIsNot(john.last_name, u'')
