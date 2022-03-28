from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class IndexPage(TemplateView):
    def get(self,request,**kwargs):
        article_data = []
        all_articles = Article.objects.order_by('-created_at').all()[:6]
        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category,
                'created_at': article.created_at.date(),
            })

        promotes_data = []
        all_promotes_data = Article.objects.filter(promote=True)
        for promote in all_promotes_data:
            promotes_data.append({
                'category': promote.category.title,
                'title': promote.title,
                'author': promote.author.user.first_name + " " + promote.author.user.last_name,
                'avatar': promote.author.avatar.url if promote.author.avatar else None,
                'cover': promote.cover.url if promote.cover.url else None,
                'created_at': promote.created_at.date(),
            })
        context = {
            'article_data' : article_data,
            'promotes_data' : promotes_data,
        }
        return render(request,'index.html',context)

class ContactPage(TemplateView):
    template_name = 'page-contact.html'

class AllArticleAPIView(APIView):
    def get(self,request,format=None):

        try:
            all_articles = Article.objects.all().order_by('-created_at')
            data = []
            for article in all_articles:
                data.append({
                    'title': article.title,
                    'cover': article.cover.url if article.cover.url else None,
                    'category': article.category.title,
                    'content': article.content,
                    'created_at': article.created_at,
                    'author': article.author.user.first_name + " " + article.author.user.last_name,
                    'promote': article.promote,
                })

            return Response({'data': data},status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Internal Server Error.'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleArticleAPIView(APIView):
    def get(self,request,format=None):
        try:
            article_title = request.GET['article_title']
            article = Article.objects.filter(title__contains=article_title)
            serialized_data = serializers.SingleArticleSerializers(article,many=True)
            data = serialized_data.data
            return Response({'data': data} , status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Internal Server Error'} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchArticleAPIView(APIView):
    def get(self,request,fromat=None):
        try:
            from django.db.models import Q
            query = request.GET['query']
            articles = Article.objects.filter(Q(content__icontains=query))
            data = []
            for article in articles:
                data.append({
                    'title': article.title,
                    'cover': article.cover.url if article.cover.url else None,
                    'content': article.content,
                    'category': article.category.title,
                    'created_at': article.created_at,
                    'author': article.author.user.first_name + " " + article.author.user.last_name,
                    'promote': article.promote,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Internal Server Error'} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)


