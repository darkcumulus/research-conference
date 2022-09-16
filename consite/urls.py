"""consite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView


from users import urls as user_urls
from conferences import urls as conference_urls

import tagulous.views
from conferences import models

urlpatterns = [
    url(r"^admin/", admin.site.urls, name="admin-home"),
    url(
        r"^api/keywords/$",
        tagulous.views.autocomplete,
        {"tag_model": models.Keyword},
        name="conference_keywords_autocomplete",
    ),
    url(r"^users/", include(user_urls, namespace="users")),
    url(r"^logout/$", auth_views.logout, {"next_page": "home"}, name="logout"),
    url(
        r"^login/$",
        auth_views.login,
        {"template_name": "registration/login.html"},
        name="login",
    ),
    url(r"^conferences/", include(conference_urls, namespace="conf")),
    # url(r'^$', RedirectView.as_view(url='/conferences/'), name='home'),
    url(r"^$", TemplateView.as_view(template_name="index.html"), name="home"),
]

if settings.DJANGO_MODE == "local":
    # import debug_toolbar

    # urlpatterns += [
    #     path("__debug__/", include(debug_toolbar.urls)),
    # ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
