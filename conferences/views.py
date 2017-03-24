from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

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