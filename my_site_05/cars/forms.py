from django import forms

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(
#         label='Write you review here', 
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'myform',
#                 'rows': '2',
#                 'cols': '2',
#             }
#         ),
#         )

from .models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # 1. pass in only the fields you want to show
        # fields = ['first_name', 'last_name']
        # 2. pass in all fields
        fields = "__all__" 
        # 3. Set field labels
        labels = {
            'first_name': 'Your First Name',
            'last_name': 'Your Last Name',
            'stars': 'Rating (1-5)',
        }

        error_messages = {
            'stars': {
                'min_value': '评分不能低于1',
                'max_value': '评分不能超过5',
            }
        }
