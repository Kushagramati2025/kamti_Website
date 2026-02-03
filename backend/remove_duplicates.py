
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import UseCase

def remove_duplicates():
    # We'll identify duplicates by title and image path
    seen = set()
    duplicates_count = 0
    
    # Get all use cases ordered by ID (so we keep the first one created)
    all_ucs = UseCase.objects.all().order_by('id')
    
    for uc in all_ucs:
        identifier = (uc.title.strip(), uc.image.name if uc.image else None)
        if identifier in seen:
            print(f"Removing duplicate: {uc.title} (ID: {uc.id})")
            uc.delete()
            duplicates_count += 1
        else:
            seen.add(identifier)
            
    print(f"\nTotal duplicates removed: {duplicates_count}")

if __name__ == '__main__':
    remove_duplicates()
