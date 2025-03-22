from django import forms
from .models import ProfileUpdate

class ResourceForm(forms.ModelForm):
    class Meta:
        model = ProfileUpdate
        fields = '__all__'