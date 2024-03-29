from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('' , views.IndexPage.as_view(),name = 'index'),
    path('contact/',views.ContactPage.as_view(), name = 'contact'),
    url('^article/all/$',views.AllArticleAPIView.as_view(),name="all_articles"),
    url('^article/$',views.SingleArticleAPIView.as_view(),name='single_article'),
    url('^article/search/$', views.SearchArticleAPIView.as_view(),name='search_article'),
    url('^article/submit/$',views.SubmitArticleAPIView.as_view(),name='submit_article'),
    url('^article/update_cover/$',views.UpdateArticleAPIView.as_view(),name="update_article"),
    url('^article/delete/$', views.DeleteArticleAPIView.as_view(), name="delete_article")
]