
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import UseCase

for uc in UseCase.objects.all():
    if "Master Use Case List" in uc.title or "Intelligent Analytics" in uc.title:
        print(f"ID: {uc.id} | Name: {uc.title} | Path: {uc.image.name}")
