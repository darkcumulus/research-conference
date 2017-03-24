from django.db import models
from django.utils import timezone
from consite.base import BaseProfile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime

class Organizer(BaseProfile):
	fullname = models.TextField(max_length=256, unique=True)
	shortname = models.CharField(max_length=10, blank=True, help_text='Shortname')
	email = models.EmailField(blank=True, help_text="Enter the official email address of the agency")
	website = models.CharField(max_length=128, blank=True, help_text="Enter the website of this Agency/Organizer/Sponsor")
	contact = models.CharField(max_length=128, blank=True, help_text='Enter Contact Numbers (separated with comma)')
	
	
	class Meta:
		verbose_name_plural = "Agencies" 
		ordering = ('fullname',)
		
	def __str__(self):
		return self.fullname

	def get_absolute_url(self):
		return reverse('organizer-detail', kwargs={'pk', self.pk})

	def save(self, *args, **kwargs):
		if (self.shortname is None):
			self.shortname = "".join(word[0] for word in self.shortname.upper().split())
		super(Organizer, self).save(*args, **kwargs)

class PendingManager(models.Manager):
	def get_queryset(self):
		return super(PendingManager,self).get_queryset().filter(start_date__gte=datetime.datetime.now())

class Conference(BaseProfile):
	LEVEL_CHOICES = (
		('0', 'unknown'),
		('1', 'local'),
		('2', 'regional'),
		('3', 'national'),
		('4', 'international'),
	)
	title = models.TextField(max_length=256, help_text='Enter conference name')
	level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default=0, help_text="What type of Conference is this?")
	registration_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, help_text="Enter the Registration Fee")
	organizers = models.ManyToManyField(Organizer, verbose_name='List of Organizers')
	venue = models.CharField(max_length=256, blank=True, help_text='Location of the event')
	poster  = models.FileField(upload_to='%Y/%m/%d/', help_text="Upload the PDF/DOCX Poster here (ZIP/RAR format)",blank=True)
	start_date = models.DateField(default=timezone.localtime(timezone.now()) + datetime.timedelta(days=30), verbose_name="Date Started")
	end_date = models.DateField(default=timezone.localtime(timezone.now()) + datetime.timedelta(days=32),verbose_name="Date Ended")
	abstract_deadline = models.DateTimeField(default=timezone.localtime(timezone.now()) + datetime.timedelta(days=15),blank=True, verbose_name="Deadline of Abstract Submission")
	paper_deadline = models.DateTimeField(default=timezone.localtime(timezone.now()) + datetime.timedelta(days=20),blank=True, verbose_name="Deadline of Paper Submission")
	contact_details = models.TextField(max_length=256, blank=True)
	description = models.TextField(max_length=512, blank=True)
	
	objects = models.Manager()
	pending = PendingManager()
	
	
	class Meta:
		ordering = ('title',)
		
		
	def __str__(self):
		return self.title

	def get_organizers_short(self):
		ret = ",".join([org.shortname for org in self.organizers.all()])
		return ret 

	def get_organizers_long(self, flag=True):
		ret = ",".join([org.fullname for org in self.organizers.all()])
		return ret

class Author(BaseProfile):
    GENDER_CHOICES = (
        ('0', 'Unknown'),
        ('1', 'male'),
        ('2', 'female'),
    )
    firstname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=0)

    class Meta:
        ordering = ('lastname',)
        unique_together = ('firstname', 'middlename', 'lastname', )

    def __str__(self):
        fullname = self.lastname + ', ' + self.firstname[0]+'.'
        return fullname

	# def get_conferences(self):
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk', self.pk})

class Study(BaseProfile):
    RESEARCH_TYPES = (
        ('0', 'unknown'),
        ('1', 'study'),
        ('2', 'project'),
    )

    PRESENTATION_TYPES = (
        ('0', 'unknown'),
        ('1', 'oral'),
        ('2', 'poster'),
    )

    title = models.CharField(max_length=256, verbose_name="Research Title", unique=True)
    authors = models.ManyToManyField(Author, verbose_name="List of authors")
    presentor = models.ForeignKey(Author, related_name="authors", blank=True, verbose_name="Presented by", null=True)
    conference = models.ForeignKey(Conference, blank=True, verbose_name="Conference Title")
    research_type = models.CharField(max_length=1, verbose_name="Type of Research", choices=RESEARCH_TYPES, default=0)
    presentation_type = models.CharField(max_length=1, verbose_name="Type of Presentation", choices=PRESENTATION_TYPES,
                                         default=0)
    other_info = models.TextField(blank=True)

    class Meta:
        ordering = ('title',)
        unique_together = ('title', 'conference')
        verbose_name_plural = 'Studies'

    def get_authors(self):
        ret = ",".join([str(author) for author in self.authors.all()])
        return ret

    def __str__(self):
        return self.title