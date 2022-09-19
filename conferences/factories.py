import factory
import datetime
import factory.fuzzy as fuzzy

from .models import Organizer, Author, Category, Comment, Study


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
# class Study(BaseProfile):
#     RESEARCH_TYPES = (
#         ("0", "unknown"),
#         ("1", "study"),
#         ("2", "project"),
#     )

#     PRESENTATION_TYPES = (
#         ("0", "unknown"),
#         ("1", "oral"),
#         ("2", "poster"),
#     )

#     title = models.CharField(max_length=256, verbose_name="Research Title", unique=True)
#     authors = models.ManyToManyField(Author, verbose_name="List of authors")
#     presentor = models.ForeignKey(
#         Author,
#         related_name="authors",
#         blank=True,
#         verbose_name="Presented by",
#         null=True,
#     )
#     conference = models.ForeignKey(
#         Conference, blank=True, verbose_name="Conference Title"
#     )
#     research_type = models.CharField(
#         max_length=1, verbose_name="Type of Research", choices=RESEARCH_TYPES, default=0
#     )
#     presentation_type = models.CharField(
#         max_length=1,
#         verbose_name="Type of Presentation",
#         choices=PRESENTATION_TYPES,
#         default=0,
#     )
#     other_info = models.TextField(blank=True)

#     class Meta:
#         ordering = ("title",)
#         unique_together = ("title", "conference")
#         verbose_name_plural = "Studies"

#     def get_authors(self):
#         ret = ",".join([str(author) for author in self.authors.all()])
#         return ret

#     def __str__(self):
#         return self.title

# import random
# class StudyFactory(factory.django.DjangoModelFactory):
#     """
#     Creates a Study object
#     """

#     class Meta:
#         model = 

#     title = None
#     authors = factory.Iterator(random.sample([Comment.objects.all()], 3))
#     presentor = factory.LazyAttribute(lambda o: )

