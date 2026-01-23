
import os
import django
import sys

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Industry, IndustrySection

def update_automotive():
    print("Updating Automotive content...")
    
    # 1. Delete existing Automotive industry to avoid duplicates
    Industry.objects.filter(name="Automotive").delete()
    print("Deleted existing Automotive data.")

    # 2. Create Automotive Industry
    automotive = Industry.objects.create(
        name="Automotive",
        description="Empowering Automakers with Next-Gen Technologies. The global automotive industry is undergoing a tremendous amount of change at an unprecedented pace. The experience of electric vehicles (EV) and autonomous vehicles (AV) is being enhanced by technological advancements, including multi-sensor, AI-enabled, over-the-air upgrades, and more. Especially with generative AI, the automotive sector has countless possibilities, from voice and virtual assistants to material and generative design.",
        banner_image="industries/banners/automotive_banner.jpg" 
    )
    print("Created Automotive Industry.")

    # 3. Create Sections
    sections = [
        {
            "title": "Predictive Maintenance & AI-Powered Solutions",
            "content": "Predictive Modelling, leveraging historical and current data to extract crucial insights can significantly enhance strategic decision-making and help businesses maintain a competitive edge. Leveraging data analytics to monitor vehicle health, anticipate failures, and reduce unplanned downtime.",
            "image": "industries/sections/auto_predictive.jpg"
        },
        {
            "title": "Connectivity & Data-Driven Service",
            "content": "Connectivity and data-driven services are transforming the automotive industry, enabling new capabilities and business models. Connected cars collect and transmit vehicle data, facilitating real-time monitoring, remote control, and the development of advanced features like over-the-air updates and predictive maintenance.",
            "image": "industries/sections/auto_connectivity.jpg"
        },
        {
            "title": "Supply Chain & Inventory Management",
            "content": "Effective inventory and supply chain management are essential for productivity and profitability in the automobile sector. This entails organizing the movement of components, parts, and completed automobiles from suppliers to consumers. Optimizing inventory levels to reduce expenses and guarantee on-time delivery to satisfy client needs is a major priority.",
            "image": "industries/sections/auto_supply_chain.jpg"
        }
    ]

    for section in sections:
        IndustrySection.objects.create(industry=automotive, **section)
        print(f"Created section: {section['title']}")

    print("Automotive content update complete.")

if __name__ == '__main__':
    update_automotive()
