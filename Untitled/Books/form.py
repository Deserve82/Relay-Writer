from django import forms

from .models import Novel


class WriteForm(forms.ModelForm):
    class Meta:
        model = Novel
        fields = ['title', 'author', 'publisher', 'novelContent', 'novelImage', 'novelPrice', 'novelCategory']

class NovelSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')