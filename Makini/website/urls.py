from django.urls import path
from . import views

app_name= 'website'
urlpatterns = [
    path('', views.Home, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('event', views.event, name='event'),
    path('courses', views.Home, name='courses'),
    path('trainers', views.trainer, name='trainers'),
    path('pricing', views.pricing, name='pricing'),

]
