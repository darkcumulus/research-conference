from django.conf.urls import url, include
from django.views.generic import TemplateView

from conferences.views import (
    ConferenceList,
    ConferenceDetail,
    ConferenceCreate,
    ConferenceUpdate,
    ConferenceDelete,
)

import tagulous.views
from conferences import models

urlpatterns = [
    url(r"^$", ConferenceList.as_view(), name="conference-list"),
    url(r"^(?P<pk>\d+)/$", ConferenceDetail.as_view(), name="conference-detail"),
    url(r"^create/$", ConferenceCreate.as_view(), name="conference-create"),
    url(r"^update/(?P<pk>\d+)/$", ConferenceUpdate.as_view(), name="conference-update"),
    url(r"^delete/(?P<pk>\d+)/$", ConferenceDelete.as_view(), name="conference-delete"),
    url(r"^categories/$", ConferenceList.as_view(), name="categories-list"),
    url(
        r"^categories/(?P<slug>[^/]+)?$",
        ConferenceList.as_view(),
        name="categories-list",
    ),
]
