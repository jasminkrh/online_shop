from django import forms
from django_shop_app.models import Rating


class RatingEditForm(forms.ModelForm):

    class Meta:

        model = Rating
        fields = ['text']

        widgets = {
            'comment_id': forms.HiddenInput(),
        }
