from django.db.utils import IntegrityError
from django.test import TestCase
from conferences.models import Organizer
from .factories import OrganizerFactory, AuthorFactory, CategoryFactory, CommentFactory

class OrganizerDatabaseTest(TestCase):
    def setUp(self):
        super(OrganizerDatabaseTest, self).setUp()

    def test_organizer_can_be_created_with_only_fullname_field_entry(self):
        organizer = OrganizerFactory(fullname="ABC Company",shortname="",email="",website="", contact="" )
        self.assertEquals(Organizer.objects.get(id=1), organizer)

    def test_organizer_cannot_be_created_with_all_entries_blank(self):
        organizer = OrganizerFactory(fullname="",shortname="",email="",website="", contact="" )
        self.assertEquals(Organizer.objects.get(id=1), organizer)

    def test_organizer_cannot_be_created_if_there_is_an_existing_organizer_with_same_fullname_in_database(self):
        organizer1 = OrganizerFactory(fullname="ABC Company",shortname="",email="",website="", contact="" )
        self.assertEquals(Organizer.objects.get(id=1), organizer1)
        self.assertRaises(IntegrityError, OrganizerFactory, fullname="ABC Company",shortname="",email="",website="", contact="" )