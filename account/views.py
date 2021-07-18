from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from account.decorator import unauthenticated_user, allowed_users, admin_only
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Group
from .decorator import admin_only
from . forms import LoginForm, RegisterForm

@unauthenticated_user
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


@unauthenticated_user
def register_view(request, *args, **kwargs):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user_obj.is_active = True
        user_obj.save()
        user_obj.set_password(password)
        user_obj.save()

        group = Group.objects.get(name='customer')
        user_obj.groups.add(group)
        
    return render(request, 'account/register.html', {'form': form})
