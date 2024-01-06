
from django import forms

class PurchaseForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
