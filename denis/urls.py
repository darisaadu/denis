"""denis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from account.views import (
    login_view,
    logout_view,
    register_view
)


from emails.views import (
    email_entry_create_view,
    email_entry_detail_view,
    email_entry_list_view,
    email_entry_delete_view,
    email_entry_update_view,
    custormer_page
)

urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('new_user_custormer_page/', custormer_page),
    path('', email_entry_create_view),
    path('emails/', email_entry_list_view),
    path('emails/<int:id>/', email_entry_detail_view),
    path('emails/<int:id>/update/', email_entry_update_view),
    path('emails/<int:id>/delete/', email_entry_delete_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG: # denotes in DEVELOPMENT not PRODUCTION!!!
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
