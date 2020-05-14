from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('our_team/',views.our_team, name='our_team'),
    path('contact/',views.contact, name='contact'),
]