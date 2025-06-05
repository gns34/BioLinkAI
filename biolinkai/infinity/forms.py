from django import forms
class BioForm(forms.Form):
    firstname=forms.CharField(max_length=200)
    lastname=forms.CharField(max_length=255)
    phoneno=forms.IntegerField(null=True)