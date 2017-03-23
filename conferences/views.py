from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Conference

import datetime

class ConferenceList(ListView):
	model = Conference
	template_name = 'conferences/index.html'
	context_object_name = 'conferences'

	# you can filter this to customise the data being outputted
	
	def get_queryset(self):
		# import pdb; pdb.set_trace()
		# return Conference.objects.filter(start_date__gte=datetime.datetime.now()).order_by('start_date')
		return Conference.objects.all()

	# uncomment below, if you want to modify, template data

	# def get_context_data(self, **kwargs):
	# 	# Call the base implementation first to get a context
	# 	context = super(ConferenceList, self).get_context_data(**kwargs)
	# 	# Get the blog from id and add it to the context
	# 	return context


class ConferenceDetail(DetailView):
	model = Conference 
	template_name = 'conferences/conference.html'

