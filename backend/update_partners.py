import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Partner

def update_partners():
    # Clear existing partners to avoid duplicates/stale data
    print("Clearing existing partners...")
    Partner.objects.all().delete()

    partners_data = [
        {"file": "Computomic-Logo.avif", "name": "Computomic", "website": "https://computomic.com"},
        {"file": "Microsoft.avif", "name": "Microsoft", "website": "https://microsoft.com"},
        {"file": "aws.avif", "name": "AWS", "website": "https://aws.amazon.com"},
        {"file": "databricks_Logo.avif", "name": "Databricks", "website": "https://databricks.com"},
        {"file": "msme.avif", "name": "MSME", "website": ""},
        {"file": "snowflake.avif", "name": "Snowflake", "website": "https://snowflake.com"},
        {"file": "Picture3.avif", "name": "Partner", "website": ""}, # Generic name
        {"file": "64b983_c80fc2054bf84c28a5f6c93b31f7f21a~mv2.avif", "name": "Partner", "website": ""},
        {"file": "64b983_d69e4578155844e295aa462d5b635bf0~mv2.avif", "name": "Partner", "website": ""},
    ]

    print("Adding partners from media/partners...")
    
    for i, p_data in enumerate(partners_data):
        # Check if file exists in media/partners
        file_path = f"partners/{p_data['file']}"
        full_path = os.path.join(os.getcwd(), 'media', 'partners', p_data['file'])
        
        if os.path.exists(full_path):
            Partner.objects.create(
                name=p_data['name'],
                logo=file_path,
                website=p_data['website'],
                order=i
            )
            print(f"Added {p_data['name']}")
        else:
            print(f"Warning: File not found for {p_data['name']}: {full_path}")

if __name__ == '__main__':
    update_partners()
