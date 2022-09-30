from django.db.utils import IntegrityError
from django.forms import ValidationError
from django.test import TestCase
from conferences.models import Organizer
from .factories import OrganizerFactory, AuthorFactory, CategoryFactory, CommentFactory


class OrganizerDatabaseTest(TestCase):
    def setUp(self):
        super(OrganizerDatabaseTest, self).setUp()

    def test_organizer_can_be_created_with_only_fullname_field_entry(self):
        organizer = OrganizerFactory(
            fullname="ABC Company", shortname="", email="", website="", contact=""
        )
        self.assertEquals(Organizer.objects.get(id=1), organizer)

    def test_organizer_cannot_be_created_with_all_entries_blank(self):
        with self.assertRaises(ValidationError):
            organizer = OrganizerFactory(
                fullname="", shortname="", email="", website="", contact=""
            )
            organizer.save()

    def test_organizer_cannot_be_created_if_there_is_an_existing_organizer_with_same_fullname_in_database(
        self,
    ):
        organizer1 = OrganizerFactory(
            fullname="ABC Company", shortname="", email="", website="", contact=""
        )
        self.assertEquals(Organizer.objects.get(id=1), organizer1)
        self.assertRaises(
            IntegrityError,
            OrganizerFactory,
            fullname="ABC Company",
            shortname="",
            email="",
            website="",
            contact="",
        )
    
    def test_organizer_shortname_is_generated_from_fullname_when_shortname_is_blank(self):
        organizer = OrganizerFactory(
            fullname="Every Good Boy Does Fine", shortname="", email="foo@gmail.com", website="", contact=""
        )
        another_organizer = OrganizerFactory(
            fullname="Coolguys Of Palawan", shortname="cgop", email="foo@gmail.com", website="", contact=""
        )
        # test if blank
        self.assertEquals(Organizer.objects.get(id=1), organizer)
        self.assertEquals(organizer.shortname, "EGBDF")

        # test if user provided explicit value
        self.assertEquals(Organizer.objects.get(id=2), another_organizer)
        self.assertEquals(another_organizer.shortname, "cgop")
