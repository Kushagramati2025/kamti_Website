
import os
import requests

def download_file(url, filepath):
    print(f"Downloading {url} to {filepath}...")
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Done.")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    media_dir = os.path.join(base_dir, 'media', 'industries')
    
    banner_dir = os.path.join(media_dir, 'banners')
    section_dir = os.path.join(media_dir, 'sections')

    os.makedirs(banner_dir, exist_ok=True)
    os.makedirs(section_dir, exist_ok=True)

    images = [
        # (URL, destination_folder, filename)
        
        # Banner: Blue/Purple Healthcare Tech
        ("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1600&q=80", 
         banner_dir, "healthcare_banner.jpg"),
         
        # Section 1: Data Insights (Tablet/Charts)
        ("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80", 
         section_dir, "data_insights.jpg"),
         
        # Section 2: Predictive (Brain/Scan)
        ("https://images.unsplash.com/photo-1530497610245-94d3c16cda28?auto=format&fit=crop&w=800&q=80", 
         section_dir, "predictive_analysis.jpg"),
         
        # Section 3: AI Chatbot (Futuristic/Robot Hand or Screen)
        ("https://images.unsplash.com/photo-1531746790731-6c087fecd65a?auto=format&fit=crop&w=800&q=80", 
         section_dir, "ai_chatbot.jpg"),
         
        # Section 4: Cost/Recommendations (Doctor/Surgery/Tech)
        ("https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=800&q=80", 
         section_dir, "cost_reduction.jpg"),

        # Section 5: X-Ray (Radiology)
        ("https://images.unsplash.com/photo-1516549655169-df83a0833860?auto=format&fit=crop&w=800&q=80", 
         section_dir, "xray.jpg"),
         
    ]
    
    # Automotive Images
    automotive_images = [
        # Banner: Sleek modern car or assembly line
        ("https://images.unsplash.com/photo-1617788138017-80ad40651399?auto=format&fit=crop&w=1600&q=80",
         banner_dir, "automotive_banner.jpg"),

        # Section 1: Predictive Maintenance (Mechanic with tablet/screen)
        ("https://images.unsplash.com/photo-1487754180451-c456f719a1fc?auto=format&fit=crop&w=800&q=80",
         section_dir, "auto_predictive.jpg"),

        # Section 2: Connectivity (Dashboard/Digital)
        ("https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=800&q=80",
         section_dir, "auto_connectivity.jpg"),

        # Section 3: Supply Chain (Factory/Robots)
        ("https://images.unsplash.com/photo-1565043666747-69f6646db940?auto=format&fit=crop&w=800&q=80",
         section_dir, "auto_supply_chain.jpg"),
    ]
    
    images.extend(automotive_images)

    # Logistics Images
    logistics_images = [
        # Banner: Global shipping or containers
        ("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1600&q=80",
         banner_dir, "logistics_banner.jpg"),

        # Section 1: Last Mile (Delivery van/GPS)
        ("https://images.unsplash.com/photo-1556740738-b6a63e27c4df?auto=format&fit=crop&w=800&q=80",
         section_dir, "logistics_last_mile.jpg"),

        # Section 2: Warehouse (Shelves/CCTV)
        ("https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=800&q=80",
         section_dir, "logistics_warehouse.jpg"),

        # Section 3: Demand Forecasting (Charts)
        ("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
         section_dir, "logistics_forecasting.jpg"),

        # Section 4: Sentiment Analysis (Case Study)
        ("https://images.unsplash.com/photo-1555421689-491a97ff2040?auto=format&fit=crop&w=800&q=80",
         section_dir, "logistics_sentiment.jpg"),
    ]
    
    images.extend(logistics_images)

    # Pharma Images
    pharma_images = [
        # Banner: Lab Test Tubes (Verified)
        ("https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&w=1600&q=80",
         banner_dir, "pharma_banner.jpg"),

        # Section 1: Data Lake / Genomics (Technology / Circuit Board)
        ("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
         section_dir, "pharma_data_lake.jpg"),

        # Section 2: Correlation Models (Microscope)
        ("https://images.unsplash.com/photo-1532187643603-ba119ca4109e?auto=format&fit=crop&w=800&q=80",
         section_dir, "pharma_models.jpg"),

        # Section 3: Drug Discovery (Medicine/Pills)
        ("https://images.unsplash.com/photo-1471864190281-a93a3070b6de?auto=format&fit=crop&w=800&q=80",
         section_dir, "pharma_drug_discovery.jpg"),

        # Section 4: Sales/Growth (Meeting/Business)
        ("https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=800&q=80",
         section_dir, "pharma_sales.jpg"),
    ]

    images.extend(pharma_images)

    # About Page Images
    about_dir = os.path.join(media_dir, 'about')
    os.makedirs(about_dir, exist_ok=True)
    
    about_images = [
        # Team / Collaboration
        ("https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1600&q=80",
         about_dir, "about_team.jpg"),
         
        # Innovation / Tech (Abstract or Chip)
        ("https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80",
         about_dir, "about_innovation.jpg"),

        # Vision / Future (Horizon or Light)
        ("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1600&q=80",
         about_dir, "about_vision.jpg"),
         
        # CEO Placeholder (Professional male)
        ("https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=800&q=80",
         about_dir, "ceo_placeholder.jpg"),
    ]

    images.extend(about_images)

    # Careers Page Images
    careers_dir = os.path.join(media_dir, 'careers')
    os.makedirs(careers_dir, exist_ok=True)

    careers_images = [
        # Banner: Diversity / Team
        ("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1600&q=80",
         careers_dir, "careers_banner.jpg"),

        # Culture: Office Fun / Collaboration
        ("https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=800&q=80",
         careers_dir, "career_culture.jpg"),

        # Growth: Ladder / Training
        ("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80",
         careers_dir, "career_growth.jpg"),
    ]
    
    images.extend(careers_images)

    for url, folder, filename in images:
        filepath = os.path.join(folder, filename)
        if not os.path.exists(filepath):
            download_file(url, filepath)
        else:
            print(f"Skipping {filename}, already exists.")

if __name__ == '__main__':
    main()
