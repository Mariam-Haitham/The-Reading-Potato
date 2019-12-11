from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all().order_by('-id')
    context = {
        "articles": articles,
    }
    return render(request, 'list.html', context)


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        "article": article,
    }
    return render(request, 'detail.html', context)