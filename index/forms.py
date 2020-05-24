from django import forms
from .models import Number

class UploadNumber(forms.ModelForm):
    class Meta:
        model = Number
        fields = ('photo',)