
import os
import django
import sys

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import UseCase

def delete_specific_usecases():
    titles_to_remove = [
        "Kushagramati Master Use Case List V1.2(1) 1",
        "Kushagramati Master Use Case List V1.2(1) 11",
        "Kushagramati Master Use Case List V1.2(1) 18",
        "Kushagramati Master Use Case List V1.2(1) 2",
        "Kushagramati Master Use Case List V1.2(1) 21",
        "Kushagramati Master Use Case List V1.2(1) 26"
    ]

    print(f"Attempting to remove {len(titles_to_remove)} specific Use Cases...")

    for title in titles_to_remove:
        # We use filter().delete() to handle cases where it might not exist or duplicates exist
        deleted_count, _ = UseCase.objects.filter(title__iexact=title).delete()
        if deleted_count > 0:
            print(f"Successfully deleted: '{title}'")
        else:
            print(f"Not found: '{title}'")

if __name__ == '__main__':
    delete_specific_usecases()
