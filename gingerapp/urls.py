from django.urls import path
from gingerapp import views

urlpatterns = [
    path('',views.home,name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('gallery',views.gallery, name='gallery')
]
