from django import forms
from .models import *


class InterestDataForm(forms.ModelForm):
    class Meta:
        model = InterestData
        fields = ["loan_date", "release_date", "principal", "rate", "total"]

    def __init__(self, *args, **kwargs):
        super(InterestDataForm, self).__init__(*args, **kwargs)

        self.fields['loan_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        self.fields['release_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        self.fields['principal'].widget.attrs['placeholder'] = 'Principal Amount'
