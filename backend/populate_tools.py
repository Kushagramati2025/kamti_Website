import os
import django
import shutil

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Tool

def populate_tools():
    # Source media path
    media_root = 'media'
    
    tools_data = [
        {
            "title": "Kushagramati Migration Accelerator",
            "description": "An accelerator for efficient migration to Databricks, featuring unified configuration, AI-driven script modification, and automated notebook generation.",
            "pdf_name": "Kushagramati Migration Accelerator  GHBW 16 September 2025 1.pdf"
        },
        {
            "title": "Platform Optimization Solution",
            "description": "Comprehensive solution for optimizing your data platform performance and costs.",
            "pdf_name": "Kushagramati Platform Optimization Solution Flyer New V1.0.pdf"
        },
        {
            "title": "Platform Tuning Services",
            "description": "Expert services to tune and refine your platform for maximum efficiency.",
            "pdf_name": "Platform Tuning Services Summary-New.pdf"
        }
    ]

    print("Populating Tools...")
    
    # Ensure target directory exists
    target_dir = os.path.join(media_root, 'tools', 'pdfs')
    os.makedirs(target_dir, exist_ok=True)

    for item in tools_data:
        # Check if already exists
        if Tool.objects.filter(title=item['title']).exists():
            print(f"Tool '{item['title']}' already exists. Skipping.")
            continue
            
        pdf_source = os.path.join(media_root, item['pdf_name'])
        
        # Check if source file exists
        if not os.path.exists(pdf_source):
            print(f"Warning: Source PDF '{item['pdf_name']}' not found in media root. Skipping.")
            continue
            
        # Copy file to formatted specific location if we want, or just link it.
        # Ideally, FileField expects file relative to MEDIA_ROOT.
        # Since the files are already in MEDIA_ROOT, we can just point to them, 
        # OR move them to tools/pdfs/ for better organization.
        # Let's move/copy them.
        
        pdf_dest_name = item['pdf_name'].replace(" ", "_")
        pdf_dest_path = os.path.join(target_dir, pdf_dest_name)
        
        shutil.copy2(pdf_source, pdf_dest_path)
        
        # Relative path for Django DB
        db_path = f"tools/pdfs/{pdf_dest_name}"
        
        Tool.objects.create(
            title=item['title'],
            description=item['description'],
            pdf_file=db_path,
            order=0
        )
        print(f"Created Tool: {item['title']}")

if __name__ == '__main__':
    populate_tools()
