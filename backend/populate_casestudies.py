import os
import django
import requests
import shutil
from django.core.files import File
from urllib.parse import urlparse

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import CaseStudy

def download_file(url, target_dir, filename=None):
    if not filename:
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename.endswith('.pdf'):
            filename += '.pdf'
            
    # Clean filename
    filename = filename.replace('%20', '_').replace(' ', '_')
    target_path = os.path.join(target_dir, filename)
    
    print(f"Downloading {url} to {target_path}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(target_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return filename, target_path
    else:
        print(f"Failed to download {url}. Status: {response.status_code}")
        return None, None

def populate_casestudies():
    # Source media path
    media_root = 'media'
    target_dir = os.path.join(media_root, 'casestudies', 'pdfs')
    os.makedirs(target_dir, exist_ok=True)
    
    studies_data = [
        {
            "title": "Optima X-Ray Predictor",
            "description": "An advanced AI solution for predictive X-ray analysis in healthcare contexts.",
            "url": "https://f352b213-7383-423f-9b34-df406a10369a.filesusr.com/ugd/ef2530_522b2dc7dfb04b7899c0d8858879d8f3.pdf",
            "filename": "Optima_XRay_Predictor.pdf"
        },
        {
            "title": "Sentiment Analysis Classification",
            "description": "Classification of text based on keywords for enhanced customer insight and data processing.",
            "url": "https://f352b213-7383-423f-9b34-df406a10369a.filesusr.com/ugd/ef2530_4935fe8a95cc468ea1f62dada0185f84.pdf",
            "filename": "Sentiment_Analysis.pdf"
        }
    ]

    print("Populating Case Studies...")

    for item in studies_data:
        # Check if already exists
        if CaseStudy.objects.filter(title=item['title']).exists():
            print(f"Case Study '{item['title']}' already exists. Skipping.")
            continue
            
        # Download
        final_filename, file_path = download_file(item['url'], target_dir, item['filename'])
        
        if final_filename:
            # Relative path for Django DB
            db_path = f"casestudies/pdfs/{final_filename}"
            
            CaseStudy.objects.create(
                title=item['title'],
                description=item['description'],
                pdf_file=db_path,
                order=0
            )
            print(f"Created Case Study: {item['title']}")

if __name__ == '__main__':
    populate_casestudies()
