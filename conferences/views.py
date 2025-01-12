from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q, Count
from django.http import Http404
from django.urls import reverse
from django import template


from .models import Conference, Category, Comment
from .forms import CommentForm
import datetime

register = template.Library()


@register.inclusion_tag("conferences/categories-list.html")
def display_cat():
    allcategories = Category.objects.all()
    return {"allcategories": allcategories}


class ConferenceList(ListView):
    model = Conference
    template_name = "conferences/index.html"
    context_object_name = "conferences"
    paginate_by = 4

    # you can filter this to customise the data being outputted

    def get_queryset(self):
        # return Conference.objects.filter(start_date__gte=datetime.datetime.now()).order_by('start_date')
        query = self.request.GET.get("q")
        # import pdb; pdb.set_trace()
        if query:
            return Conference.objects.filter(
                Q(title__icontains=query)
                | Q(venue__icontains=query)
                | Q(contact_details__icontains=query)
                | Q(description__icontains=query)
                # | Q(keywords__slug__icontains=query)
            ).order_by("-created")
        if self.kwargs and self.kwargs["slug"]:
            query = Conference.objects.filter(
                categories__slug=self.kwargs["slug"]
            ).order_by("-created")
            if query:
                return query
        return Conference.objects.all().order_by("-created")

    # uncomment below, if you want to modify, template data

    def get_context_data(self, **kwargs):
        context = super(ConferenceList, self).get_context_data(**kwargs)
        # import pdb; pdb.set_trace()
        context["object"] = {"cats": Category.objects.all()}
        return context


class ConferenceDetail(DetailView):
    model = Conference
    template_name = "conferences/conference.html"

    def get_gdrive_poster_link(self, url):
        import re

        if url != None:
            try:
                # find an alphanumeric string having 28 chars in URL
                found = re.search("([a-zA-Z0-9]{28})", url)
                url = "https://drive.google.com/uc?export=download&id=" + found.group(1)
            except AttributeError:
                # if not found then provide empty link
                found = ""
        else:
            url = "#"
        # import pdb; pdb.set_trace()
        return url

    def post(self, request, pk):
        comment_form = CommentForm(request.POST)
        # import pdb; pdb.set_trace()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            if request.user.username:
                new_comment.name = request.user.username
                new_comment.email = request.user.email
            else:
                new_comment.name = "anonymous"
                new_comment.email = "noemail@gmail.com"

            new_comment.conference = self.get_object()
            new_comment.active = True
            new_comment.save()
        return redirect(reverse("conf:conference-detail", args=(pk,)))

    def get_context_data(self, **kwargs):
        context = super(ConferenceDetail, self).get_context_data(**kwargs)

        url = context["conference"].poster_file_url

        # import pdb; pdb.set_trace()
        context["object"].download_url = self.get_gdrive_poster_link(url)
        context["object"].cats = Category.objects.all()

        context["comment_form"] = CommentForm
        context["comments"] = context["conference"].comments.filter(active=True)

        # get similar conferences
        keyword_ids = context["conference"].keywords.values_list("id", flat=True)
        similar_conferences = Conference.objects.filter(
            keywords__in=keyword_ids
        ).exclude(id=context["conference"].id)
        similar_conferences = similar_conferences.annotate(
            same_keywords=Count("keywords")
        ).order_by("-same_keywords", "-start_date")[:4]
        context["similar_conferences"] = similar_conferences

        return context


class ConferenceCreate(LoginRequiredMixin, CreateView):
    # tell that youre happy
    model = Conference
    fields = (
        "title",
        "poster_image",
        "level",
        "registration_fee",
        "organizers",
        "venue",
        "poster_file_url",
        "start_date",
        "end_date",
        "abstract_deadline",
        "paper_deadline",
        "contact_details",
        "description",
    )
    template_name = "conferences/create.html"
    success_url = "conferences/index.html"


class ConferenceUpdate(LoginRequiredMixin, UpdateView):
    model = Conference
    fields = (
        "title",
        "poster_image",
        "level",
        "registration_fee",
        "organizers",
        "venue",
        "poster_file_url",
        "start_date",
        "end_date",
        "abstract_deadline",
        "paper_deadline",
        "contact_details",
        "description",
    )
    template_name = "conferences/update.html"
    success_url = "conferences/index.html"

    def get_object(self, queryset=None):
        obj = super(ConferenceUpdate, self).get_object()
        if not self.request.user.has_perm(
            "conferences.conference.can_change_conference"
        ):
            raise Http404
        return obj


class ConferenceDelete(LoginRequiredMixin, DeleteView):
    model = Conference
    template_name = "conferences/delete.html"
    success_url = "conferences/index.html"

    def get_object(self, queryset=None):
        obj = super(ConferenceDelete, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj


class HomeView(TemplateView):
    template_name = "index.html"
