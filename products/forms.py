from django import forms


class ProductCreateForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()


class ReviewCreateForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
