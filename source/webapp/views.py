from django.shortcuts import render
from webapp.models import Article


def index_view(request, *args, **kwargs):
    articles = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': articles
    })


def article_view(request, *args, **kwargs):
    article_id = request.GET.get('id')
    article = Article.objects.get(pk=article_id)
    return render(request, 'article.html', context={
        'article': article
    })


def article_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        text = request.POST.get('text')
        article = Article.objects.create(title=title, author=author, text=text)
        return render(request, 'article.html', {'article': article})
