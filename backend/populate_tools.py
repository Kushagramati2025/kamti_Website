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
            "description": "A holistic solution to analyze and enhance your data ecosystem. We identify bottlenecks, optimize cloud usage, and implement cost-saving strategies to ensure maximum value.",
            "pdf_name": "Kushagramati Platform Optimization Solution Flyer New V1.0.pdf"
        },
        {
            "title": "Platform Tuning Services",
            "description": "Specialized deep-dive performance tuning. From query optimization to cluster configuration, we fine-tune every layer of your platform to achieve high throughput and low latency.",
            "pdf_name": "Platform Tuning Services Summary-New.pdf"
        }
    ]

    print("Populating Tools...")
    
    # clear existing tools to ensure updates are applied
    Tool.objects.all().delete()
    print("Cleared existing tools.")

    # Ensure target directory exists
    target_dir = os.path.join(media_root, 'tools', 'pdfs')
    os.makedirs(target_dir, exist_ok=True)

    for item in tools_data:
        pdf_source = os.path.join(media_root, item['pdf_name'])
        
        # Check if source file exists
        if not os.path.exists(pdf_source):
            print(f"Warning: Source PDF '{item['pdf_name']}' not found in media root. Skipping.")
            # Fallback: try to find it in tools/pdfs if it was already moved
            existing_dest = os.path.join(target_dir, item['pdf_name'].replace(" ", "_"))
            if os.path.exists(existing_dest):
                print(f"Found existing file at {existing_dest}, using it.")
                pdf_dest_path = existing_dest
                pdf_dest_name = item['pdf_name'].replace(" ", "_")
            else:
                continue
        else:
             # Copy file
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
