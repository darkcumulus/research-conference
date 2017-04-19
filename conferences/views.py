from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.http import Http404


from .models import Conference
import datetime

class ConferenceList(ListView):
	model = Conference
	template_name = 'conferences/index.html'
	context_object_name = 'conferences'
	paginate_by = 4 

	# you can filter this to customise the data being outputted
	
	def get_queryset(self):
		# return Conference.objects.filter(start_date__gte=datetime.datetime.now()).order_by('start_date')
		query = self.request.GET.get("q")	
		if query:
			return Conference.objects.filter(
				Q(title__icontains=query) |
				Q(venue__icontains=query) |
				Q(contact_details__icontains=query) |
				Q(description__icontains=query) 
				).order_by('-start_date')
		return Conference.objects.all().order_by('-start_date')
		

	# uncomment below, if you want to modify, template data

	# def get_context_data(self, **kwargs):
	# 	# Call the base implementation first to get a context
	# 	context = super(ConferenceList, self).get_context_data(**kwargs)
	# 	# Get the blog from id and add it to the context
	# 	return context


class ConferenceDetail(DetailView):
	model = Conference 
	template_name = 'conferences/conference.html'

	def get_context_data(self, **kwargs):
		import re
		context = super(ConferenceDetail, self).get_context_data(**kwargs)
		url = context['conference'].poster_file_url
			
		if url != None:
			try:
				#find an alphanumeric string having 28 chars in URL
				found = re.search('([a-zA-Z0-9]{28})',url)
			except AttributeError:
				#if not found then provide empty link
				found = '#'
			url = 'https://drive.google.com/uc?export=download&id='+found.group(1)
		# import pdb; pdb.set_trace()	
		context['download_url'] = url 
		return context



class ConferenceCreate(LoginRequiredMixin, CreateView):
	# tell that youre happy
	model = Conference
	fields = (
			'title',
			'poster_image',
			'level',
			'registration_fee',
			'organizers',
			'venue',
			'poster_file_url',
			'start_date',
			'end_date',
			'abstract_deadline',
			'paper_deadline',
			'contact_details',
			'description',
	)	
	template_name = 'conferences/create.html'
	success_url = 'conferences/index.html'

class ConferenceUpdate(LoginRequiredMixin, UpdateView):
	model = Conference 
	fields = (
			'title',
			'poster_image',
			'level',
			'registration_fee',
			'organizers',
			'venue',
			'poster_file_url',
			'start_date',
			'end_date',
			'abstract_deadline',
			'paper_deadline',
			'contact_details',
			'description',
	)
	template_name = 'conferences/update.html'
	success_url = 'conferences/index.html'

	def get_object(self, queryset=None):
		obj = super(ConferenceUpdate, self).get_object()
		if not obj.owner == self.request.user:
			raise Http404
		return obj

class ConferenceDelete(LoginRequiredMixin, DeleteView):
	model = Conference 
	template_name = 'conferences/delete.html'
	success_url = 'conferences/index.html'

	def get_object(self, queryset=None):
		obj = super(ConferenceDelete, self).get_object()
		if not obj.owner == self.request.user:
			raise Http404
		return obj


class HomeView(TemplateView):
	template_name = "index.html"