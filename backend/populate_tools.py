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
            "title": """<span class="text-brand-purple">Kushagra</span><span class="text-brand-orange">mati</span> Migration Accelerator""",
            "description": "An accelerator for efficient migration to Databricks, featuring unified configuration, AI-driven script modification, and automated notebook generation.",
            "content": """
<h3>Accelerate Your Move to Databricks</h3>
<p>The <span class="text-brand-purple">Kushagra</span><span class="text-brand-orange">mati</span> Migration Accelerator is designed to simplify and speed up your migration journey to the Databricks Lakehouse Platform. By automating complex tasks, we reduce migration time by up to 40%.</p>

<h4>Key Features:</h4>
<ul>
    <li><strong>Unified Configuration Management:</strong> Centralized control over all migration parameters.</li>
    <li><strong>AI-Driven Code Conversion:</strong> Automatically converts legacy SQL/Python scripts to optimized Spark code.</li>
    <li><strong>Automated Notebook Generation:</strong> Creates Databricks notebooks ready for immediate use.</li>
    <li><strong>Data Validation Framework:</strong> Built-in checks to ensure data integrity pre- and post-migration.</li>
</ul>

<h4>Benefits:</h4>
<ul>
    <li>Reduced Risk of Human Error</li>
    <li>Faster Time-to-Value</li>
    <li>Cost-Effective Migration Strategy</li>
</ul>
""",
            "pdf_name": "Kushagramati Migration Accelerator  GHBW 16 September 2025 1.pdf"
        },
        {
            "title": "Platform Optimization Solution",
            "description": "A holistic solution to analyze and enhance your data ecosystem. We identify bottlenecks, optimize cloud usage, and implement cost-saving strategies to ensure maximum value.",
            "content": """
<h3>Maximize ROI on Your Data Platform</h3>
<p>Our Platform Optimization Solution provides a 360-degree view of your data infrastructure health. We go beyond simple monitoring to provide actionable insights for tuning and cost reduction.</p>

<h4>What We Analyze:</h4>
<ul>
    <li>Compute Utilization & auto-scaling patterns</li>
    <li>Storage Lifecycle policies and tiering</li>
    <li>Query Performance and indexing strategies</li>
    <li>Security & Access Control audits</li>
</ul>

<h4>The Outcome:</h4>
<p>Clients typically see a <strong>20-30% reduction in cloud costs</strong> and a significant improvement in job reliability and performance.</p>
""",
            "pdf_name": "Kushagramati Platform Optimization Solution Flyer New V1.0.pdf"
        },
        {
            "title": "Platform Tuning Services",
            "description": "Specialized deep-dive performance tuning. From query optimization to cluster configuration, we fine-tune every layer of your platform to achieve high throughput and low latency.",
            "content": """
<h3>Deep-Dive Performance Engineering</h3>
<p>When 'good enough' isn't enough, our Platform Tuning Services extract every ounce of performance from your data platform. Ideal for mission-critical SLAs and high-frequency data applications.</p>

<h4>Our Approach:</h4>
<ul>
    <li><strong>Cluster Sizing:</strong> Right-sizing instance types and worker counts.</li>
    <li><strong>Spark Config Tuning:</strong> Optimizing shuffle partitions, memory fraction, and serialization.</li>
    <li><strong>Data Layout Optimization:</strong> Z-Ordering, Partitioning, and File Compaction strategies.</li>
    <li><strong>Code Profiling:</strong> Identifying hotspots in your ETL pipelines.</li>
</ul>

<p><em>Get the performance you paid for. Eliminate waste and latency.</em></p>
""",
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
            content=item.get('content', ''),
            pdf_file=db_path,
            order=0
        )
        print(f"Created Tool: {item['title']}")

if __name__ == '__main__':
    populate_tools()
