from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article

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