from django.contrib import admin
from .models import Conference, Organizer, Study, Author

class AuthorAdmin(admin.ModelAdmin):
	model = Author
admin.site.register(Author, AuthorAdmin)

class StudyAdmin(admin.ModelAdmin):
	model = Study
admin.site.register(Study, StudyAdmin)

class OrganizerAdmin(admin.ModelAdmin):
	model = Organizer 
	
admin.site.register(Organizer, OrganizerAdmin)

class ConferenceAdmin(admin.ModelAdmin):
	model = Conference 
	list_display = ('id','title', 'level','registration_fee', 'venue', 'start_date', 'end_date', 'abstract_deadline', 'paper_deadline',)
	search_fields = ('title','venue',)
	ordering = ['start_date','title']
	list_filter = ('level', 'start_date')
	
	
admin.site.register(Conference, ConferenceAdmin)