import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Industry, CaseStudy

def link_case_studies():
    print("Linking Case Studies to Industries...")
    
    # 1. Healthcare -> Optima X-Ray Predictor
    try:
        healthcare = Industry.objects.get(name__iexact="Healthcare")
        optima = CaseStudy.objects.get(title__icontains="Optima X-Ray")
        healthcare.case_study = optima
        healthcare.save()
        print(f"Linked '{optima.title}' to '{healthcare.name}'")
    except Industry.DoesNotExist:
        print("Healthcare industry not found.")
    except CaseStudy.DoesNotExist:
        print("Optima X-Ray case study not found.")

    # 2. Logistics -> Sentiment Analysis (Assuming this mapping based on user request)
    # The user mentioned "http://localhost:4200/industries/logistics" and "Sentiment analysis"
    try:
        logistics = Industry.objects.get(name__iexact="Logistics")
        sentiment = CaseStudy.objects.get(title__icontains="Sentiment Analysis")
        logistics.case_study = sentiment
        logistics.save()
        print(f"Linked '{sentiment.title}' to '{logistics.name}'")
    except Industry.DoesNotExist:
        print("Logistics industry not found.")
    except CaseStudy.DoesNotExist:
        print("Sentiment Analysis case study not found.")

if __name__ == '__main__':
    link_case_studies()
