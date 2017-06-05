from django.contrib import admin
from .models import Conference, Organizer, Study, Author, Category, Comment

import tagulous.admin 
from conferences import models 

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'body', 'conference', 'created', 'active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'created', 'updated')
	search_fields = ('name',)
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

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
	list_display = ('id','title', 'level','registration_fee', 'venue', 'start_date', 'end_date', 'abstract_deadline', 'paper_deadline','keywords')
	search_fields = ('title','venue',)
	ordering = ['start_date','title']
	list_filter = ('level', 'start_date')
tagulous.admin.register(models.Conference, ConferenceAdmin)	

# Auto-gen the ModelAdmin for keywords 
tagulous.admin.register(models.Keyword)

#admin.site.register(Conference, ConferenceAdmin)
