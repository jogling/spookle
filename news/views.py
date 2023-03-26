from django.shortcuts import render, get_object_or_404
from .models import Article

def news_detail(request, article_id):
    print(article_id)  # add this line to print the article_id parameter
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news/news_detail.html', {'article': article})