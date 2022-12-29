from django import forms

class URLForm(forms.Form):
   long_url = forms.CharField(label='long_url', max_length=200)