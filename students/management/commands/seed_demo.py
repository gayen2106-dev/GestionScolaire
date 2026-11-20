"""Charge des données fictives (6 étudiants, 3 enseignants) pour tester le site.

Usage : python manage.py seed_demo
La commande peut être relancée sans créer de doublons (basée sur l'email).
"""
from django.core.management.base import BaseCommand

from students.models import Student
from teachers.models import Teacher

STUDENTS = [
    ("Awa", "Diop", "awa.diop@ecole.sn", "L1", True, "771234567"),
    ("Moussa", "Fall", "moussa.fall@ecole.sn", "L2", True, ""),
    ("Fatou", "Ndiaye", "fatou.ndiaye@ecole.sn", "L1", False, ""),
    ("Ibrahima", "Sow", "ibrahima.sow@ecole.sn", "L3", True, ""),
    ("Mariama", "Ba", "mariama.ba@ecole.sn", "L2", True, ""),
    ("Ousmane", "Cissé", "ousmane.cisse@ecole.sn", "L3", True, ""),
]

TEACHERS = [
    ("Mamadou", "Ba", "mamadou.ba@ecole.sn", "Mathématiques"),
    ("Aïssatou", "Sy", "aissatou.sy@ecole.sn", "Informatique"),
    ("Cheikh", "Diallo", "cheikh.diallo@ecole.sn", "Anglais"),
]


class Command(BaseCommand):
    help = "Charge des étudiants et des enseignants fictifs."

    def handle(self, *args, **options):
        created = 0
        for first, last, email, classe, active, phone in STUDENTS:
            _, is_new = Student.objects.get_or_create(
                email=email,
                defaults={
                    "first_name": first, "last_name": last, "classe": classe,
                    "active": active, "phone": phone,
                },
            )
            created += is_new
        for first, last, email, subject in TEACHERS:
            _, is_new = Teacher.objects.get_or_create(
                email=email,
                defaults={"first_name": first, "last_name": last, "subject": subject},
            )
            created += is_new
        self.stdout.write(self.style.SUCCESS(f"{created} enregistrement(s) créé(s)."))
