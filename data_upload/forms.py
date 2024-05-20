from django import forms
from django.contrib.auth.models import User
from .models import QueryBuilderData
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password',]
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None


class QueryBuilderForm(forms.ModelForm):
    class Meta:
        model = QueryBuilderData
        fields = ['keyword', 'industry', 'year_founded', 'city', 'state', 'country', 'employee_from', 'employee_to']

class QueryForm(forms.Form):
    keyword = forms.CharField(max_length=255, required=False)
    industry = forms.CharField(max_length=255, required=False)
    year_founded = forms.ChoiceField(choices=[], required=False)
    city = forms.CharField(max_length=255, required=False)
    state = forms.CharField(max_length=255, required=False)
    country = forms.CharField(max_length=255, required=False)
    employee_from = forms.CharField(max_length=255, required=False)
    employee_to = forms.CharField(max_length=255, required=False)

    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.fields['year_founded'].choices = self.get_year_choices()


