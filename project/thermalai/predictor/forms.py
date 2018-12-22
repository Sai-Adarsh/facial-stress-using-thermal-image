from django import forms

class GetPictureForm(forms.Form):
	
	file  = forms.FileField(max_length=100)