
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import UseCase

def update_all_usecases():
    # 1. Remove cover/category/contact slides
    to_remove_indicators = [
        "Intelligent Analytics-1.jpg",
        "Intelligent Analytics-7.jpg",
        "Kushagramati Master Use Case List V1.2(1)-1.jpg",
        "Kushagramati Master Use Case List V1.2(1)-2.jpg",
        "Kushagramati Master Use Case List V1.2(1)-11.jpg",
        "Kushagramati Master Use Case List V1.2(1)-18.jpg",
        "Kushagramati Master Use Case List V1.2(1)-21.jpg",
        "Kushagramati Master Use Case List V1.2(1)-26.jpg",
    ]
    
    for img_name in to_remove_indicators:
        UseCase.objects.filter(image__icontains=img_name).delete()
        print(f"Removed cover/category slide: {img_name}")

    # 2. Update Titles mapping (using image name as key for precision)
    title_mapping = {
        # Intelligent Analytics folder
        "Intelligent Analytics-2.jpg": "Financial Loan Management System",
        "Intelligent Analytics-3.jpg": "Leave Management System",
        "Intelligent Analytics-4.jpg": "KMATI Accelerator (Migration tool)",
        "Intelligent Analytics-5.jpg": "Real-Time Products Recommendation System",
        "Intelligent Analytics-6.jpg": "Databrick workflow Framework",
        
        # Master Use Case List folder
        "Kushagramati Master Use Case List V1.2(1)-3.jpg": "Optimizing Robotic Telemetry Data Processing for Healthcare",
        "Kushagramati Master Use Case List V1.2(1)-4.jpg": "Creating Data Pipelines for Large Data",
        "Kushagramati Master Use Case List V1.2(1)-5.jpg": "Migration to Databricks Workspace 2.0 for Advanced Analytics",
        "Kushagramati Master Use Case List V1.2(1)-6.jpg": "Migration from Synapse to Databricks using BladeBridge",
        "Kushagramati Master Use Case List V1.2(1)-7.jpg": "Migration from GCP to Azure Databricks",
        "Kushagramati Master Use Case List V1.2(1)-8.jpg": "Migration from Oracle to Azure Databricks",
        "Kushagramati Master Use Case List V1.2(1)-9.jpg": "Migration from Informatica SQL to Azure Databricks",
        # 10 and 12 were already done but let's include for completeness/safety
        "Kushagramati Master Use Case List V1.2(1)-10.jpg": "Migration from Cloudera to Databricks",
        "Kushagramati Master Use Case List V1.2(1)-12.jpg": "Contracts Data Integration and BI Reporting - SAP data to databricks",
        
        "Kushagramati Master Use Case List V1.2(1)-13.jpg": "Creating Data Pipelines for Call Center Conversations",
        "Kushagramati Master Use Case List V1.2(1)-14.jpg": "Scalable Data Pipeline for Customer Information Processing",
        "Kushagramati Master Use Case List V1.2(1)-15.jpg": "Real Time Streaming for Quotes and Policy for an US Insurance Company",
        "Kushagramati Master Use Case List V1.2(1)-16.jpg": "Implementing Unified Data Platform for an Airline Company",
        "Kushagramati Master Use Case List V1.2(1)-17.jpg": "Implementing AI/ML Solution for Airline Operations",
        "Kushagramati Master Use Case List V1.2(1)-19.jpg": "Migrating from HMS to Databricks Unity Catalog for Large Pharma company",
        "Kushagramati Master Use Case List V1.2(1)-20.jpg": "Migrating from legacy to Databricks Unity Catalog for US Insurance Company",
        "Kushagramati Master Use Case List V1.2(1)-22.jpg": "Increasing Job Success Rate",
        "Kushagramati Master Use Case List V1.2(1)-23.jpg": "Improved Performance for Queries",
        "Kushagramati Master Use Case List V1.2(1)-24.jpg": "Optimized Resource Utilization",
        "Kushagramati Master Use Case List V1.2(1)-25.jpg": "Data Re-partitioning",
    }

    print("\nUpdating titles...")
    for img_key, new_title in title_mapping.items():
        ucs = UseCase.objects.filter(image__icontains=img_key)
        if ucs.exists():
            for uc in ucs:
                uc.title = new_title
                uc.save()
                print(f"Updated: {img_key} -> {new_title}")
        else:
            print(f"Warning: Image key {img_key} not found in database.")

if __name__ == '__main__':
    update_all_usecases()
