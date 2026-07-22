"""
URL configuration for core project.
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('', include('dashboard.urls')),
    path('', include('notifications.urls')),
    path('', login_required(lambda request: redirect('sgdh:dashboard')), name='home'),
]
