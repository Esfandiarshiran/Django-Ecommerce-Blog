from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import login, get_user_model, authenticate, logout, update_session_auth_hash
from django.contrib.auth.models import User
from Ecommerce_setting.models import SiteSetting
from django.contrib.auth.decorators import login_required
from Ecommerce_setting.models import SiteSetting
from django.contrib import messages


# Creat login view
def login_user(request):
    # Start adding fetch and set social media addresses----------
    url = SiteSetting.objects.first()
    facebook_url = url.facebook
    twitter_url = url.twitter
    instagram_url = url.instagram
    # End adding fetch and set social media addresses----------

    if request.user.is_authenticated:
        return redirect('/dashboard')
    # Create or Clean data login form
    login_form = LoginForm(request.POST or None)
    # how to login user

    if login_form.is_valid():
        UserName = login_form.cleaned_data.get('user_name')
        Password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=UserName, password=Password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'You\'re login successfully!')
                return redirect('/dashboard')
            else:
                return HttpResponse('Sorry! your account is disabled')
        else:
            login_form.add_error('user_name', 'Invalid login')
    # Pass Data to log in templates
    context = {
        'login_form': login_form,
        'facebook_url': facebook_url,
        'twitter_url': twitter_url,
        'instagram_url': instagram_url,
    }

    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            # As a first step we don't save it in the DataBase, and just save it in memory
            # with commit = False in order to check repassword
            new_user = register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data['password'])
            # Save in DB
            new_user.save()
            # User.objects.create_user(username=user_name, email=email, password=password)
            return render(request, 'accounts/register_done.html', {'new_user': new_user})

    else:
        register_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'register_form': register_form})


def log_out(request):
    logout(request)
    return redirect('/account/login')


@login_required()
def change_password(request):
    message = ""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Use built in method for updating user data
            message = 'Your password has been successfully updated. Pay attention to rules please!'
            return redirect('account/password_change/done')
        else:
            message = Exception('Your password has not been successfully updated!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form,
        'message': message,
    })


# Retrieve Terms of service to show in its page

def terms_of_service(request):
    rules = SiteSetting.objects.first()
    rules = rules.terms_of_service

    return render(request, 'accounts/terms_of_service.html', {'rules': rules})


@login_required()
def change_password_done(request):
    return render(request, 'accounts/password_change_done.html')
