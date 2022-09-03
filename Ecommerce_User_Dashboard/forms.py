from django import forms
from .models import UserProfile
from captcha.fields import CaptchaField


# class ProfileForm(forms.Form):
#     first_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'placeholder': 'Enter your First Name '}),
#         label='First Name:',
#         max_length= 100,
#         validators=[
#             validators.MaxLengthValidator(150, 'Your full name must be less than 100 characters')
#         ]
#     )
#     last_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'placeholder': 'Enter your Last Name '}),
#         label='First Name:',
#         max_length= 100,
#         validators=[
#             validators.MaxLengthValidator(150, 'Your full name must be less than 100 characters')
#         ]
#     )
#
#
#     phone = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder':  'Enter your Phone Number'}),
#         label='Phone Number',
#         max_length=30,
#         validators=[
#             validators.MaxLengthValidator(200, 'Your subject must be less than 30 characters')
#         ]
#     )
#     talk = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder':  'Introduce Your self in one line'}),
#         label='Talk About Yourself',
#         max_length=500,
#         validators=[
#             validators.MaxLengthValidator(200, 'Your subject must be less than 200 characters')
#         ]
#     )
#     country = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'placeholder': 'Enter your country'}),
#         label='First Name:',
#         max_length= 100,
#         validators=[
#             validators.MaxLengthValidator(150, 'Your full name must be less than 100 characters')
#         ]
#     )
#     sex = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'placeholder': 'Enter your Full Name ', 'class': 'form-control'}),
#         label='First Name:',
#         max_length= 100,
#         validators=[
#             validators.MaxLengthValidator(150, 'Your full name must be less than 100 characters')
#         ]
#     )
#
#     picture = forms.ImageField(
#         widget=forms.FileInput(attrs={'placeholder': 'Upload Your Picture'}),
#         labale='Profile Picture',
#     )

class ProfileForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'mobile', 'talk',
                  'country', 'update_date', 'profile_picture', 'sex',
                  'email','birth_day', 'mobile','phone','programmer',]
