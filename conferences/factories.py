import factory
import datetime
import factory.fuzzy as fuzzy

from .models import Organizer, Author, Category, Comment


class OrganizerFactory(factory.django.DjangoModelFactory):
    """
    Creates an Organizer.
    """

    class Meta:
        model = Organizer

    fullname = factory.Faker("company", locale="en_PH")
    # shortname = None
    email = factory.Faker("ascii_email", locale="en_PH")
    website = factory.Faker("url", locale="en_PH")
    contact = factory.Faker("globe_mobile_number", locale="en_PH")


class AuthorFactory(factory.django.DjangoModelFactory):
    """
    Creates an author
    """

    class Meta:
        model = Author

    firstname = factory.Faker("first_name", locale="en_PH")
    middlename = factory.Faker("last_name", locale="en_PH")
    lastname = factory.Faker("last_name", locale="en_PH")
    gender = fuzzy.FuzzyChoice([0, 1, 2])


class CategoryFactory(factory.django.DjangoModelFactory):
    """
    Creates a Category
    """

    class Meta:
        model = Category

    name = factory.Faker("word")
    slug = factory.LazyAttribute(lambda o: "%s-slug" % o.name)
    description = factory.Faker("sentence", locale="en_PH")


class CommentFactory(factory.django.DjangoModelFactory):
    """
    Creates a Comment, requires which conference to create comment on
    >c1 = Conference.objects.all()[0]
    >CommentFactory.create_batch(3, conference=c1)
    """

    class Meta:
        model = Comment

    conference = None
    name = factory.Faker("name")
    email = factory.Faker("safe_email")
    body = factory.Faker("sentence", nb_words=6)
    active = True


# TODO ConferenceFactory
# TODO StudyFactory
