from django.conf.urls import url
from django.urls import path

from . import views

#
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
#

from .views import SignUpView

urlpatterns = [
    path('',  views.HomePageView.as_view(), name='index'),
    path('user/', login_required(views.ProfileView.as_view()), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
