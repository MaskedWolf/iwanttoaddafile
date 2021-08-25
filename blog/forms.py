from django import forms

class ActivityForm(forms.Form):
    shopname = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )

    # descriptions = forms.TextField(widget=forms.Textarea(
    #     attrs={
    #         "class": "form-control",
    #         "placeholder": "Leave a comment!"
    #     })
    # )

    # author = forms.CharField(
    #     max_length=255,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Your Name"
    #     })
    # )

    # author = forms.CharField(
    #     max_length=255,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Your Name"
    #     })
    # )

    # category
    # state
    # image

  # category = models.ManyToManyField('Category', related_name='activity')
  # state = models.ManyToManyField('State', related_name='activity')
  # image = models.ImageField(upload_to='picture/')
