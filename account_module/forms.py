from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    last_name = forms.CharField(
        label='نام خانوادگی',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    phone = forms.CharField(
        label='شماره تماس',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(11)
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]

    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return password
        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password == new_password:
            return new_password
        else:
            ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')
