from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


from . forms import LoginForm, RegisterForm


def login_view(request, *args, **kwargs):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user == None:
            return redirect('/login')

        login(request, user)
        return redirect('/')
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login')


def register_view(request, *args, **kwargs):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user_obj.is_active = False
        user_obj.save()
        user_obj.set_password(password)
        user_obj.save()
    return render(request, 'account/register.html', {'form': form})
