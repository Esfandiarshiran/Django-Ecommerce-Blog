from django import forms
from django.contrib.auth.models import User
from django.core import validators
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your UserName'}),
        label='User Name:'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": 'Enter your password'}),
        label='Password:'
    )
    captcha = CaptchaField(
        label='Captcha:'
    )



    # Also we can handel forms and do validation here befor this line in views(not recommended ):
    # login_form.is_valid():
    # to be exact at this line:
    # login_form = LoginForm(request.POST or None)
    # just we need to import User


# this way is not recommended
# def clean_user_name(self):
#     user_name = self.cleaned_data.get('user_name')
#     is_exists_user = User.objects.filter(username=user_name).exists()
#     if not is_exists_user:
#         raise forms.ValidationError('The User Name is invalid')
#     return user_name


#################################################################################

# class RegisterForm(forms.Form):
#     user_name = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'Enter your user name'}),
#         label='User Name',
#         validators=[
#             validators.MaxLengthValidator(limit_value=20,
#                                           message='user name should be lees than 20 characters'),
#             validators.MinLengthValidator(3, 'user name should be more than 3 characters')
#         ]
#     )
#
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email'}),
#         label='Email',
#         validators=[
#             validators.EmailValidator('Email is not valid')
#         ]
#     )
#
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
#         label='Password'
#     )
#
#     re_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again'}),
#         label='Re-type Password'
#     )
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         is_exists_user_by_email = User.objects.filter(email=email).exists()
#         if is_exists_user_by_email:
#             raise forms.ValidationError('The Email already is exist')
#
#         if len(email) > 30:
#             raise forms.ValidationError('user name should be less than 30 characters')
#
#         return email
#
#     def clean_user_name(self):
#         user_name = self.cleaned_data.get('user_name')
#         is_exists_user_by_username = User.objects.filter(username=user_name).exists()
#
#         if is_exists_user_by_username:
#             raise forms.ValidationError('The user was already registered')
#
#         return user_name
#
#     def clean_re_password(self):
#         password = self.cleaned_data.get('password')
#         re_password = self.cleaned_data.get('re_password')
#         # print(password)
#         # print(re_password)
#
#         if password != re_password:
#             raise forms.ValidationError('Passwords are not matched')
#
#         return password


class UserRegistrationForm(forms.ModelForm):
    # Add extra fild
    # Not that the built-in password doesn't have re_password

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        label='Password'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again'}),
        label='Re-type Password'
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_re_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['re_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['re_password']

    captcha = CaptchaField()
    # this built in form has all essential features
