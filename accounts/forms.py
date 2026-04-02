from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class PhoneNumberSignupForm(UserCreationForm):
    # Field 1: Phone Number (Username)
    username= forms.CharField(
        label="Phone Number",
        max_length=10,
        min_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. 0712345678'})
    )

    def clean(self):
        cleaned_data = super().clean()
        # 1. Get the actual password using the key "password1"
        password = cleaned_data.get("password1") 
        
        # 2. Check the variable you just created (password)
        if password and len(password) < 8:
            self.add_error('password1', "Password is too weak! Use at least 8 characters.")
            
        return cleaned_data