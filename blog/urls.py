from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('' , views.IndexPage.as_view(),name = 'index'),
    path('contact/',views.ContactPage.as_view(), name = 'contact')
]