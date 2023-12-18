from django import forms


class ShowProd(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.IntegerField()
    count = forms.IntegerField()
