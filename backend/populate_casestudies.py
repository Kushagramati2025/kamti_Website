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
            "content": """
<h3>Revolutionizing Radiology with AI</h3>
<p>The Optima X-Ray Predictor leverages deep learning convolutional neural networks (CNNs) to assist radiologists in detecting anomalies with higher accuracy and speed.</p>

<h4>Problem Statement:</h4>
<p>Radiologists often face high workloads, leading to fatigue and potential diagnostic errors. Early detection of conditions like Pneumonia or nodules is critical but challenging in standard X-rays.</p>

<h4>Our Solution:</h4>
<ul>
    <li><strong>Automated Screening:</strong> Pre-screens X-rays to flag potential issues before a doctor reviews them.</li>
    <li><strong>Heatmap Visualization:</strong> Highlights suspicious regions on the image using Grad-CAM technology.</li>
    <li><strong>Integration:</strong> Seamlessly integrates with existing PACS (Picture Archiving and Communication Systems).</li>
</ul>

<h4>Results:</h4>
<p>Achieved a <strong>94% accuracy rate</strong> in detecting common chest pathologies and reduced reporting turnaround time by 50%.</p>
""",
            "url": "https://f352b213-7383-423f-9b34-df406a10369a.filesusr.com/ugd/ef2530_522b2dc7dfb04b7899c0d8858879d8f3.pdf",
            "filename": "Optima_XRay_Predictor.pdf"
        },
        {
            "title": "Sentiment Analysis Classification",
            "description": "Classification of text based on keywords for enhanced customer insight and data processing.",
            "content": """
<h3>Understanding Customer Voice at Scale</h3>
<p>In the digital age, customer feedback is abundant but unstructured. Our Sentiment Analysis engine processes thousands of reviews, tweets, and emails to gauge public opinion in real-time.</p>

<h4>Methodology:</h4>
<p>We utilize Natural Language Processing (NLP) techniques, including Tokenization, Lemmatization, and Bag-of-Words models, trained on domain-specific datasets.</p>

<h4>Key Capabilities:</h4>
<ul>
    <li><strong>Aspect-Based Sentiment:</strong> Identifies sentiment towards specific product features (e.g., "Display is great, but battery is bad").</li>
    <li><strong>Real-time Monitoring:</strong> Dashboard alerts for sudden spikes in negative sentiment.</li>
    <li><strong>Multi-language Support:</strong> Capable of processing English, Spanish, and French feedback.</li>
</ul>

<h4>Impact:</h4>
<p>Enabled a leading retailer to identify a product defect within 48 hours of launch, saving an estimated $2M in potential returns and brand damage.</p>
""",
            "url": "https://f352b213-7383-423f-9b34-df406a10369a.filesusr.com/ugd/ef2530_4935fe8a95cc468ea1f62dada0185f84.pdf",
            "filename": "Sentiment_Analysis.pdf"
        }
    ]

    print("Populating Case Studies...")
    
    # Clear existing to allow updates
    CaseStudy.objects.all().delete()
    print("Cleared existing case studies.")

    # Check for file existence before downloading
    for item in studies_data:
        target_path = os.path.join(target_dir, item['filename'])
        
        if os.path.exists(target_path):
             print(f"File {item['filename']} already exists. Skipping download.")
             final_filename = item['filename']
        else:
             final_filename, file_path = download_file(item['url'], target_dir, item['filename'])
        
        if final_filename:
            # Relative path for Django DB
            db_path = f"casestudies/pdfs/{final_filename}"
            
            CaseStudy.objects.create(
                title=item['title'],
                description=item['description'],
                content=item.get('content', ''),
                pdf_file=db_path,
                order=0
            )
            print(f"Created Case Study: {item['title']}")

if __name__ == '__main__':
    populate_casestudies()
