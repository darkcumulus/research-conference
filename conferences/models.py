from django.db import models
from django.utils import timezone
from confsite.base import BaseProfile
from django.utils.text import slugify
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
	organizers = models.ManyToManyField(Organizer, null=True, verbose_name='List of Organizers')
	venue = models.CharField(max_length=256, blank=True, help_text='Location of the event')
	poster  = models.FileField(upload_to='%Y/%m/%d/', help_text="Upload the PDF/DOCX Poster here (ZIP/RAR format)",blank=True)
	start_date = models.DateField(default=timezone.localtime(timezone.now()) + datetime.timedelta(days=30), verbose_name="Date Started")
	end_date = models.DateField(default=timezone.localtime(timezone.now()) + datetime.timedelta(days=32),verbose_name="Date Ended")
	abstract_deadline = models.DateField(default=timezone.localtime(timezone.now()) + datetime.timedelta(days=15), verbose_name="Deadline of Abstract Submission")
	paper_deadline = models.DateField(default=timezone.localtime(timezone.now()) + datetime.timedelta(days=20), verbose_name="Deadline of Paper Submission")
	contact_details = models.TextField(max_length=256, blank=True)
	
	objects = models.Manager()
	pending = PendingManager()
	
	
	class Meta:
		ordering = ('title',)
		
		
	def __str__(self):
		return self.title