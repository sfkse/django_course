from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all-meetups'),
    path('<slug:meetup_slug>/success', views.register_success, name='registration-success'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]
