from django import forms
import datetime
from .models import Novel, Book


class WriteForm(forms.ModelForm):
    class Meta:
        model = Novel
        fields = ['title', 'author', 'publisher', 'novelContent', 'novelImage', 'novelPrice', 'novelCategory']

class CompileForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'editor', 'editDate', 'bookImage', 'bookPrice', 'contents', 'bookCategory']

    editDate = forms.DateField(initial=datetime.date.today,widget=forms.DateInput(attrs={'required': 'required', }))
    
class NovelSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')