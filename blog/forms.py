from django import forms
from .models import Category

class ActivityForm(forms.Form):
    shopname = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Activity Name",
        })
    )
    
    descriptions = forms.CharField(
        max_length=4000,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Descriptions"
        })
    )
    
    states = (
        ('1', 'Johor'),
        ('2', 'Kedah'),
        ('3', 'Kelantan'),
        ('4', 'Malacca'),
        ('5','Negeri Sembilan'),
        ('6', 'Pahang'),
        ('7', 'Penang'), 
        ('8', 'Perak'),
        ('9', 'Perlis'),
        ('10', 'Sabah'),
        ('11', 'Sarawak'),
        ('12', 'Selangor'),
        ('13', 'Terengganu'),
        ('14', 'Kuala Lumpur'),
        ('15', 'Labuan'),
        ('16', 'Putrajaya'),
    )

    state = forms.ChoiceField(choices=states)

    # category = forms.CharField(
    #     max_length=255,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Category"
    #     })
    # )

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    image = forms.ImageField()

class search(forms.Form):
  keyword = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
            "class": "form-control search-text",
            "placeholder": "Search...",
            "style": "color: black;",
        }))