from django.conf.urls import url, include
from django.views.generic import TemplateView

from conferences.views import ConferenceList, ConferenceDetail

urlpatterns = [
	url(r'^$', ConferenceList.as_view(), name='conference-list'),
	url(r'^(?P<pk>[0-9]+)/$', ConferenceDetail.as_view(),name='conference-detail'),

]