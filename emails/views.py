from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import HttpResponse, Http404

from . models import EmailEntry
from .forms import EmailEntryForm, EmailEntryUpdateForm
# Create your views here.

# @login_required
@staff_member_required(login_url='/login')
def email_entry_update_view(request, id=None, *args, **kwargs):
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404

    form = EmailEntryUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() 
    return render(request, 'emails/update.html', {'form': form, 'obj': obj})


# @login_required
# @staff_member_required(login_url='/login')
def email_entry_create_view(request, *args, **kwargs):
    context = {}
    if request.user.is_authenticated:
        context['some_cool_staff'] = "whatever"
    print(request.user, request.user.is_authenticated)
    form = EmailEntryForm(request.POST or None)
    context['form'] = form
    if form.is_valid():
        form.save()
        form = EmailEntryForm()
        context['added'] = True
        context['form'] = form
    return render(request, 'home.html', context)


# @login_required
@staff_member_required(login_url='/login')
def email_entry_list_view(request, *args, **kwargs):
    queryset = EmailEntry.objects.all()
    context = {'object_list': queryset}
    return render(request, 'emails/list.html', context)


# @login_required
@staff_member_required(login_url='/login')
def email_entry_detail_view(request, id=None, *args, **kwargs):
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404
    context = {'obj': obj}
    return render(request, 'emails/detail.html', context)


# @login_required
@staff_member_required(login_url='/login')
def email_entry_delete_view(request, id=None, *args, **kwargs):
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        obj.delete()
        return redirect('/emails')
    return render(request, 'emails/delete.html', {'obj': obj})