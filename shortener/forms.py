from django import forms
from .models import urls

class urls_form(forms.ModelForm):
	class Meta:
		model = urls
		fields = ('long_url','short_url')