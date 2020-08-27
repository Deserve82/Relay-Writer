from django import forms
from .models import Novel
import datetime

class WriteForm(forms.ModelForm):
    class Meta:
        model = Novel
        fields = ['title', 'writingDate', 'novelContent',  'novelImage', 'novelPrice']
    writing_date= forms.DateField(initial=datetime.date.today,widget=forms.DateInput(attrs={'required': 'required', }))

class Category(forms.ModelForm):
    option = (
        ("첫번째", "세계문학전집"),
        ("두번째", "인문"),
        ("세번째", "철학"),
        ("네번째", "종교"),
        ("다섯번째", "사회"),
        ("여섯번째", "에세이"),
        ("일곱번째", "과학"),
        ("여덟번째", "역사"),
        ("아홉번째", "경제경영"),
        ("열번째", "자기계발"),
        ("열한번째", "여행"),
        ("열두번째", "라이프스타일"),
        ("열세번째", "부모"),
        ("열넷번째", "어린이와청소년"),
        ("열다섯번째", "판타지와무협"),
        ("열여섯번째", "로맨스"),
        ("열일곱번째", "만화"),
        ("열여덟번째", "애니메이션"),
    )
    new_category = forms.ChoiceField(required=True, choices=option)