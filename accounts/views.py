from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegularUserSignUpForm, OrganizationSignUpForm
from .models import CustomUser
# Create your views here.

def signup_choice(request):
    return render(request, 'accounts/signup_choice.html')

def regular_user_signup_view(request):
    if request.method == 'POST':
        form = RegularUserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            #TODO: check if redirecting to homepage is correct
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegularUserSignUpForm()
    return render(request, 'accounts/regular_user_signup.html', {'form': form, 'user_type': 'regular'})

def organization_signup_view(request):
    if request.method == 'POST':
        form = OrganizationSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = OrganizationSignUpForm()
    return render(request, 'accounts/organization_signup.html', {'form': form, 'user_type': 'organization'})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('/')

#TODO: add a view for profile page
