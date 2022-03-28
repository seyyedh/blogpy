from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('' , views.IndexPage.as_view(),name = 'index'),
    path('contact/',views.ContactPage.as_view(), name = 'contact'),
    url('^article/all/$',views.AllArticleAPIView.as_view(),name="all_articles"),
    url('^article/$',views.SingleArticleAPIView.as_view(),name='single_article'),
]