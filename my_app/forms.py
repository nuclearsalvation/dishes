from django import forms

class DishForm(forms.Form):
    name = forms.CharField(max_length=20)
    time = forms.DecimalField(decimal_places=1, max_digits=3)
    description = forms.TextField()
    body = forms.TextField()
    img = forms.ImageField()