from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('service/',views.services,name="service"),
    path('shop/',views.shop,name="shop"),
    path('contact/',views.contact,name="contact"),
]