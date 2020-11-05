from django.views.generic import TemplateView, ListView
from django.db.models import Q

#from .models import ListaPrac, Praca, Uczen, Wydzial
from django.contrib.auth import get_user_model

from django.shortcuts import render
from datetime import date, datetime
from django.views.generic.edit import FormMixin


class HomePageView(TemplateView):
    template_name = 'index.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'