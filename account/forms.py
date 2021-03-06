from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))



class RegisterForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Comfirm password'}))


    class Meta:
        model = User
        fields = ['username', 'email']


    def clean(self):
        data = self.cleaned_data
        password_1 = data.get('password')
        password_2 = data.get('password2')
        if password_1 != password_2:
            # raise forms.ValidationError('Passwords much match.')
            self.add_error('password', 'Passwords much match.')
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            # raise forms.ValidationError(f"{email} is token. Try again.")
            self.add_error('email', f"{email} is token. Try again.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            # raise forms.ValidationError(f"{username} is token. Try again.")
            self.add_error('username', f"{username} is token. Try again.")
        return username