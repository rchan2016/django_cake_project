from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Enter a valid email address')
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=False)
    phone_number = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'phone_number')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")

        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise ValidationError("Phone number should only be digits.")

        return phone_number

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.email = self.clean_data['email']
    #     user.first_name = self.clean_data['first_name']
    #     user.last_name = self.clean_data['last_name']
    #     user.phone_number = self.clean_data['phone_number']
    #     if commit:
    #         user.save()
    #     return user
