from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('user/admin/send-notification/', views.send_notification, name='send_notification'),
]
