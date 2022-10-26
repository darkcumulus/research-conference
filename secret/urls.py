from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.secret_page, name="secret_page_inside"),
]
