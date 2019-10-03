from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import CommentForm, ArticleCommentForm
from webapp.models import Comment, Article
from .base_views import ListView, CreateView


class CommentListView(ListView):
    context_key = 'comments'
    model = Comment
    template_name = 'comment/list.html'


class CommentForArticleCreateView(CreateView):
    template_name = 'comment/create.html'
    form_class = ArticleCommentForm

    def form_valid(self, form):
        article_pk = self.kwargs.get('pk')
        article = get_object_or_404(Article, pk=article_pk)
        article.comments.create(**form.cleaned_data)
        return redirect('article_view', pk=article_pk)


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment/create.html'
    form_class = CommentForm

    def get_redirect_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})
