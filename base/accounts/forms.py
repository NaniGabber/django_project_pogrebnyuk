from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists!")
        return email
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get("email")
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    new_password = forms.CharField(required=False, widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ["username", "email"]

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get("new_password")
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "bio",
            "avatar",
            "birth_date",
            "gender",
            "email_notifications",
            "location",
        ]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
            "location": forms.TextInput(attrs={"placeholder": "City, country"}),
        }

        labels = {
            "avatar": "Your avatar",
            "birth_date": "Your birth date",
            "gender": "Gender",
            "email_notifications": "Receive news and updates to your email",
            "location": "Your location",
        }

        help_text = {
            "bio": "Please, input your name and surname",
            "birth_date": "Please, input your birth date",
        }
