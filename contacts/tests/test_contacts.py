from django.test import TestCase
from contacts.models import Person


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name="John", last_name="Doe")
        Person.objects.create(first_name="Jane", middle_name="Patterson", last_name="Doe")
        Person.objects.create(first_name="Mark")

    def test_person_all_fields(self):
        jane = Person.objects.get(first_name="Jane")
        self.assertNotEqual(jane.first_name, u'')
        self.assertEqual(jane.last_name, u'Doe')
        self.assertNotEqual(jane.middle_name, u'')

    def test_person_first_name_only(self):
        mark = Person.objects.get(first_name="Mark")
        self.assertNotEqual(mark.first_name, u'')
        self.assertEqual(mark.last_name, u'')
        self.assertEqual(mark.middle_name, u'')

    def test_person_no_last_name(self):
        john = Person.objects.get(first_name="John")
        self.assertEqual(john.middle_name, u'')
        self.assertEqual(john.first_name, u'John')
        self.assertEqual(john.last_name, u'Doe')
