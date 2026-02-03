
import os
import django
import glob
import re

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import UseCase

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

def populate():
    # 1. Clear existing use cases
    # UseCase.objects.all().delete() # Assuming we want to keep clearing or appending? 
    # User said "remove all use case content for this" in previous turn which I did.
    # So I'll assume we start fresh or append. Since I already cleared, I'll just append.
    
    # 2. Find Intelligent Analytics folder
    ia_folders = glob.glob(os.path.join(MEDIA_ROOT, "*Intelligent Analytics*"))
    print(f"Found IA folders: {ia_folders}")
    
    for folder in ia_folders:
        if os.path.isdir(folder):
            process_folder(folder, 'AI_APP_DEV')

    # 3. Find Kushagramati Master Use Case List folder
    km_folders = glob.glob(os.path.join(MEDIA_ROOT, "*Kushagramati Master Use Case List*"))
    print(f"Found KM folders: {km_folders}")
    
    for folder in km_folders:
        if os.path.isdir(folder):
            # This folder name might be very long/weird, but glob handles it.
            process_folder(folder, 'DATABRICKS')

def process_folder(folder_path, category):
    # Get all images
    images = glob.glob(os.path.join(folder_path, "*.[jJ][pP][gG]")) + \
             glob.glob(os.path.join(folder_path, "*.[pP][nN][gG]")) + \
             glob.glob(os.path.join(folder_path, "*.[aA][vV][iI][fF]"))
    
    print(f"Processing {len(images)} images in {folder_path} as {category}")
    
    for img_path in images:
        filename = os.path.basename(img_path)
        # Construct relative path for Django ImageField
        # folder_path is absolute, MEDIA_ROOT is absolute.
        # We need path relative to MEDIA_ROOT.
        
        # Check if folder is directly inside MEDIA_ROOT
        rel_folder = os.path.relpath(folder_path, MEDIA_ROOT)
        rel_img_path = os.path.join(rel_folder, filename)
        
        # Derive title from filename
        # Remove extension
        name_no_ext = os.path.splitext(filename)[0]
        # Replace special chars with spaces
        title = name_no_ext.replace('-', ' ').replace('_', ' ')
        # Remove common prefixes/suffixes if any, or just keep it simple.
        
        # Create UseCase
        UseCase.objects.create(
            title=title,
            category=category,
            image=rel_img_path, # This assumes the file is already in media root, which it is.
            challenge="Refer to the slide image for details.",
            solution="Refer to the slide image for details.",
            approach="Refer to the slide image for details.",
            benefits="Refer to the slide image for details."
        )
        print(f"Created UseCase: {title}")

if __name__ == '__main__':
    populate()
