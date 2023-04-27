from django import forms

class formContact(forms.Form):

    name= forms.CharField(label='Name', required=True)
    email = forms.CharField(label='Email', required=True)
    context = forms.CharField(label='Context', widget=forms.Textarea)
