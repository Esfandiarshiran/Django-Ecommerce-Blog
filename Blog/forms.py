import validators as validators
from django import forms
from .models import Comment


# Initial Forms based on our model
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50, label='Name')
    email = forms.EmailField(label='Email')
    to = forms.EmailField(label='To')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='Comments')

# Comment Form (Just using modelForm to prevent from extera code)
class CommentForm(forms.ModelForm):
    # an Amazing way to create a form based on our model with all their all features and limitation
    # in this case just we need these three field
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

# single form fr searching
class SearchForm(forms.Form):
    words = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Search Posts Here...', 'class': 'form-control'}),
        label='Search',
        max_length= 100,
    )
