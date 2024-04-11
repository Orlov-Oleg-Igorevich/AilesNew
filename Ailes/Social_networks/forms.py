from django import forms
from .models import PersonInfo


class PersonForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = ['firstname', 'lastname', 'date_of_birth', 'slug', 'photo']
        widgets = {'date_of_birth': forms.SelectDateWidget(years=[i for i in range(1900, 2025)])}
