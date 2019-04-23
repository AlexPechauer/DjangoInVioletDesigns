from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name:','id':'name'}))
    email = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email:','id':'email'}))
    subject = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Subject:','id':'subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'5', 'id':'message'}))
