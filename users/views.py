from django.shortcuts import render, redirect


from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms
from users.forms import UserCreationForm


class Dashboard(
    LoginRequiredMixin,
    SelectRelatedMixin,
    generic.DetailView
):
    model = User
    select_related = ('conference',)
    template_name = 'users/dashboard.html'

    def get_object(self, queryset=None):
        return self.request.user


class LogoutView(LoginRequiredMixin, generic.FormView):
    form_class = forms.LogoutForm
    template_name = 'users/logout.html'

    def form_valid(self, form):
        logout(self.request)
        return HttpResponseRedirect(reverse('home'))


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'
    #success_url = reverse_lazy('users:dashboard')

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        #import pdb; pdb.set_trace()
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit = False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            # confirm password
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError(self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )                
                
            user.set_password(password2)
            user.first_name = firstname 
            user.last_name = lastname
            user.save()

            # returns User objects if credentials are correct 
            user = authenticate(username=username, password=password2)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('users:dashboard')
        return render(request, self.template_name, {'form': form})



