
import os
import django
import sys

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Industry, IndustrySection

def restore_xray_section():
    print("Restoring Optima x-ray predictor section...")
    
    try:
        healthcare = Industry.objects.get(name="Healthcare")
        
        # Check if already exists to avoid duplicates
        if IndustrySection.objects.filter(industry=healthcare, title="Optima x-ray predictor").exists():
            print("Section already exists. Updating content...")
            section = IndustrySection.objects.get(industry=healthcare, title="Optima x-ray predictor")
            section.content = "Case Study: Identifying between cancers and healthy anatomy with 3D radiological images to enable medical experts.<br><br><a href='#' class='btn-primary'>Download Case Study</a>"
            section.image = "industries/sections/xray.jpg"
            section.save()
            print("Updated existing section.")
        else:
            IndustrySection.objects.create(
                industry=healthcare,
                title="Optima x-ray predictor",
                content="Case Study: Identifying between cancers and healthy anatomy with 3D radiological images to enable medical experts.<br><br><a href='#' class='btn-primary'>Download Case Study</a>",
                image="industries/sections/xray.jpg"
            )
            print("Created new section.")
            
    except Industry.DoesNotExist:
        print("Healthcare industry not found!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    restore_xray_section()
