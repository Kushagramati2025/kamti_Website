
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

    for url, folder, filename in images:
        filepath = os.path.join(folder, filename)
        if not os.path.exists(filepath):
            download_file(url, filepath)
        else:
            print(f"Skipping {filename}, already exists.")

if __name__ == '__main__':
    main()
