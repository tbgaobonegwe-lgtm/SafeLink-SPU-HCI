from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import PhoneNumberSignupForm  # Using your specific SPU form

# 1. LANDING PAGE (Home) - Public for Accessibility
def home_view(request):
    # This ensures residents of Galeshewe can see the dashboard immediately
    return render(request, 'accounts/home.html')

# 2. SIGNUP VIEW - Merged and Cleaned
def signup_view(request):
    if request.method == 'POST':
        form = PhoneNumberSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = PhoneNumberSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

# 3. LOGIN VIEW - With Redirect Logic
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Sends user back to the report page if that's where they came from
            return redirect(request.GET.get('next', 'home'))
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# 4. LOGOUT VIEW - Crucial for User Control
def logout_view(request):
    logout(request)
    return redirect('home')

# 5. REPORT VIEW - Protected for Security
@login_required(login_url='login')
def report_view(request):
    detected_location = "Sol Plaatje University - Main Campus (Zone 1)"
    return render(request, 'accounts/report.html', {'location': detected_location})

# 6. ALERTS VIEW - Public Visibility
def alerts_view(request):
    return render(request, 'accounts/alerts.html')

from django.contrib.auth import logout # Make sure this import is at the top!

def logout_view(request):
    logout(request)
    return redirect('home')