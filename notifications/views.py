from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from .models import Notification

User = get_user_model()


def is_admin(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_admin)
def send_notification(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if not user_id or not subject or not message:
            messages.error(request, 'Tous les champs sont obligatoires.')
            return redirect('notifications:send_notification')

        try:
            recipient = User.objects.get(pk=user_id)
            Notification.objects.create(
                recipient=recipient,
                subject=subject,
                message=message
            )
            messages.success(request, f'Notification envoyée à {recipient.get_full_name() or recipient.email}.')
        except User.DoesNotExist:
            messages.error(request, 'Utilisateur introuvable.')

        return redirect('notifications:send_notification')

    users = User.objects.filter(is_active=True).order_by('last_name', 'first_name')
    return render(request, 'sgdh/send_notification.html', {
        'users': users,
    })
