from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from main.views import ContactCreate, success

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', ContactCreate.as_view(), name='contact_page'),
    path('success/', success, name='success_page'),
    path('about-us', views.about, name='about'),
    path('section1', views.section1, name='section1'),
    path('section2', views.section2, name='section2'),
    path('section3', views.section3, name='section3'),
    path('section4', views.section4, name='section4'),
    path('section5', views.section5, name='section5'),
    path('section6', views.section6, name='section6'),
    path('section7', views.section7, name='section7'),
    path('test', views.test, name='test')
]
