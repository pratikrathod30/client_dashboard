from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('contact/', views.submit_contact, name='submit_contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
