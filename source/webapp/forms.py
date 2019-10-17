from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Article, Comment, STATUS_ACTIVE


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['created_at', 'updated_at']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) <= 10:
            raise ValidationError('This field value should be more than 10 symbols long.',
                                  code='too_short')
        return title

    def clean(self):
        super().clean()
        if self.cleaned_data.get('text') == self.cleaned_data.get('title'):
            raise ValidationError('Article text should not duplicate article title',
                                  code='title_text_duplicate')
        return self.cleaned_data.get('text')


class CommentForm(forms.ModelForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['article'].queryset = Article.objects.filter(status=STATUS_ACTIVE)

    # article = forms.ModelChoiceField(queryset=Article.objects.filter(status=STATUS_ACTIVE), label='Статья')

    class Meta:
        model = Comment
        exclude = ['created_at', 'updated_at']


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")
