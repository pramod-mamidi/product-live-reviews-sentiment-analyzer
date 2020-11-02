from django import forms

class ConForm(forms.Form):
    link= forms.CharField(label=".",widget=forms.TextInput(attrs={'class':'link','placeholder':'Name of the Product'}))
