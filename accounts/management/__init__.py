from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Initialise les rôles (Groupes Django) du SGDH'

    ROLES = [
        'Demandeur',
        'Responsable_Hierarchique',
        'Proprietaire_Ressource',
        'Admin_Habilitations',
        'RSSI',
        'Super_Admin',
    ]

    def handle(self, *args, **options):
        for role in self.ROLES:
            group, created = Group.objects.get_or_create(name=role)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Rôle créé : {role}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Rôle existant : {role}')
                )
        self.stdout.write(self.style.SUCCESS('Initialisation des rôles terminée.'))
