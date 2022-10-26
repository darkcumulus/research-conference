from django.conf.urls import url 
from . import views

#  base64_pattern = r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
#  url(r"^_b64/(?P<base64string>{})'.format(base64_pattern)", views.secret_page, name="secret_page"),
    #  url(r"^(?P<md5string>[0-9a-fA-F]{32})/", views.secret_page, name="secret_page"),

urlpatterns = [
    url(r"", views.secret_page, name="secret_page"),
]
