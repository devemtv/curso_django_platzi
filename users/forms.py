"""Forms Users"""

from django import forms


class ProfileForms(forms.Form):
    biography = forms.CharField(max_length=500, required=False)
    website = forms.URLField(max_length=200, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
