from django import forms

class ActivityForm(forms.Form):
    shopname = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Activity Name"
        })
    )
    
    descriptions = forms.CharField(
        max_length=4000,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Descriptions"
        })
    )


    # this is probably wrong
    image = forms.ImageField()
    
    states = (
      ('JOHOR', 'Johor'),
      ('KEDAH', 'Kedah'),
      ('KELANTAN', 'Kelantan'),
      ('MALACCA', 'Malacca'),
      ('NEGERI SEMBILAN','Negeri Sembilan'),
      ('PAHANG', 'Pahang'),
      ('PENANG', 'Penang'),
      ('PERAK', 'Perak'),
      ('PERLIS', 'Perlis'),
      ('SABAH', 'Sabah'),
      ('SARAWAK', 'Sarawak'),
      ('SELANGOR', 'Selangor'),
      ('TERENGGANU', 'Terengganu'),
      ('KUALA LUMPUR', 'Kuala Lumpur'),
      ('LABUAN', 'Labuan'),
      ('PUTRAJAYA', 'Putrajaya'),
    )

    state = forms.ChoiceField(choices=states)

    category = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Category"
        })
    )