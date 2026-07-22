from django.urls import path
from . import views

app_name = 'sgdh'

urlpatterns = [
    path('connexion/', views.login_view, name='login'),
    path('tableau-de-bord/', views.dashboard_view, name='dashboard'),
    path('demandes/nouvelle/', views.new_request_view, name='new_request'),
    path('demandes/', views.requests_list_view, name='requests_list'),
    path('validations/', views.validation_queue_view, name='validation_queue'),
    path('audit/', views.audit_view, name='audit'),
    path('workflows/', views.workflow_view, name='workflow'),
    path('utilisateurs/', views.users_view, name='users'),
    path('parametres/', views.settings_view, name='settings'),
]
