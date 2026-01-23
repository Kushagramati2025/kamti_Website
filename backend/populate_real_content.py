
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import ServiceCategory, LeadershipMember, VisionMission, SiteSetting, Banner

def populate():
    print("Populating COMPREHENSIVE real content...")

    # 1. Services & Industry Solutions
    # Merging Services and Industries as ServiceCategories for now to ensure they appear on the site
    services_data = [
        {
            "name": "Application Services",
            "description": "Strong blend of industry knowledge, technical skills, and project management expertise. Highly differentiated to modernize applications and accelerate the transition to the cloud. We help you build and manage cloud-native applications, migrate legacy systems, and integrate disparate systems for seamless operations.",
            "icon": "code", 
        },
        {
            "name": "Data Analytics",
            "description": "Expertise in delivering measurable and quantifiable business value. Extensive prowess in providing faster-to-market solutions using custom-built tools/platforms. We empower you with data insights that drive increased efficiency, cost savings, and optimal business decisions.",
            "icon": "chart-bar",
        },
        {
            "name": "Embedded Consultancy",
            "description": "Strategic consulting for technology integration and operational efficiency across various sectors. We specialize in Automotive & IoT (Semiconductors, Testing), PLM & PES, and provide dedicated sourcing models to meet your specific engineering needs.",
            "icon": "chip",
        },
        {
            "name": "Healthcare Solutions",
            "description": "Focuses on provider analytics, patient care optimization, and operational efficiency through intelligent data insights. We help healthcare organizations leverage data to improve patient outcomes and streamline operations.",
            "icon": "heart",
        },
        {
            "name": "Automotive Solutions",
            "description": "Specializes in connected vehicle technology, telematics data processing, and digital retail transformation. We enable automotive companies to harness the power of data for smarter vehicles and better customer experiences.",
            "icon": "truck",
        },
        {
            "name": "Logistics Solutions",
            "description": "Optimizing last-mile delivery with GPS data processing. Smart warehouse surveillance for threat detection. AI-powered demand forecasting to reduce errors by 30-50% and missed sales by 65%. Sentiment analysis for customer feedback.",
            "icon": "globe",
        },
         {
            "name": "Pharma Solutions",
            "description": "Advanced analytics for drug discovery, clinical trial monitoring, and supply chain transparency. We assist pharmaceutical companies in accelerating time-to-market and ensuring regulatory compliance through data-driven strategies.",
            "icon": "beaker",
        }
    ]

    ServiceCategory.objects.all().delete()
    for svc in services_data:
        ServiceCategory.objects.create(name=svc['name'], description=svc['description'])
    print(f"Created {len(services_data)} services/industries.")

    # 2. Leadership
    leadership_data = [
        {
            "name": "Dr. Anant R. Koppar",
            "position": "CEO & Founder",
            "bio": "A visionary technocrat and serial entrepreneur with over 3 decades of experience in the IT industry. Founder of Kshema Technologies and KTwo Technologies. He was the first CEO in India to receive PMP certification. Recipient of the Karnataka Rajyotsava Award for his contributions to the IT sector.",
        },
        {
            "name": "Vishwanath Honnungar",
            "position": "CTO",
            "bio": "Expert in Cloud Computing, AI, and Big Data with over 24 years of experience. He has been the lead architect for large-scale digital transformation projects and focuses on driving technical innovation to help clients build an insight-driven culture.",
        },
        {
            "name": "Pradeep N",
            "position": "Industry Expert and Operations",
            "bio": "Focuses on business operations, industry-specific solution design, and operational excellence. He brings deep domain expertise to ensure that our solutions meet the specific needs of our clients in various sectors.",
        },
        {
             "name": "Dayanand Yardi",
             "position": "Finance and Administration",
             "bio": "Leads the Finance and Administration functions, ensuring robust financial health and operational smoothness for the organization.",
        },
        {
             "name": "Shruthi Malagi",
             "position": "Business Development",
             "bio": "Leads Business Development initiatives, fostering strategic partnerships and driving growth by identifying new market opportunities and client needs.",
        }
    ]

    LeadershipMember.objects.all().delete()
    for leader in leadership_data:
        LeadershipMember.objects.create(name=leader['name'], position=leader['position'], bio=leader['bio'])
    print(f"Created {len(leadership_data)} leaders.")

    # 3. Vision & Mission & Values
    # Storing Values in VisionMission for now, distinct by type if possible or appending. 
    # The Model 'type' field might be restricted, let's check basic Mission/Vision first.
    
    VisionMission.objects.all().delete()
    VisionMission.objects.create(
        type='Mission', 
        content="To be a globally dominant platform-based services company in chosen industry segments by 2025. We strive to enhance the quality of life by building world-class products and solutions through the innovative application of technology. To become the most treasured business partner."
    )
    VisionMission.objects.create(
        type='Vision', 
        content="To help companies make data-driven decisions. To be a dream destination for innovators. To be a predominantly employee-owned organization."
    )
    print("Updated Vision and Mission.")

    # 4. Site Settings (Contact Info)
    SiteSetting.objects.all().delete()
    SiteSetting.objects.create(
        site_name="KMATI",
        contact_email="sales@kmati.in",
        contact_phone="9148544466",
        address="#2nd Floor, No.16, 17th Cross, M C Road, Near Maruthi Mandir, Vijayanagar, Bangalore – 560040"
    )
    print("Updated Site Settings.")

    # 5. Update Banners
    # Ensure page banners exist
    banner_configs = [
        ('HOME', 'Data-Driven Decisions', 'Helping clients build an insight-driven culture for better business.'),
        ('ABOUT', 'About KMATI', 'A team of serial entrepreneurs and domain experts.'),
        ('SERVICES', 'Our Expertise', 'From Cloud Strategy to AI/ML Modelling and Industry Solutions.'),
        ('CONTACT', 'Get in Touch', 'Visit us in Vijayanagar, Bangalore.'),
        ('INDUSTRIES', 'Industry Solutions', 'Specialized solutions for Healthcare, Automotive, Logistics, and Pharma.'),
        ('CAREERS', 'Join Us', 'Freedom to innovate and recognition of individual brilliance.'),
        ('BLOG', 'Insights', 'Latest updates and thought leadership.'),
    ]

    for type_code, title, subtitle in banner_configs:
        if not Banner.objects.filter(page=type_code).exists():
             Banner.objects.create(
                title=title,
                subtitle=subtitle,
                page=type_code,
                image=f'banners/{type_code.lower()}_default.jpg' 
            )
    
    # 6. Partners
    # Databricks is a known partner
    partners_data = [
        {"name": "Databricks", "website": "https://databricks.com"},
        {"name": "Microsoft Azure", "website": "https://azure.microsoft.com"},
        {"name": "AWS", "website": "https://aws.amazon.com"},
        {"name": "Google Cloud", "website": "https://cloud.google.com"},
    ]
    
    # Check if Partner model exists imported (it wasn't in top import, adding it)
    from core.models import Partner, CareerJob, BlogPost

    Partner.objects.all().delete()
    for p in partners_data:
        Partner.objects.create(name=p['name'], website=p['website'])
    print(f"Created {len(partners_data)} partners.")

    # 7. Careers
    jobs_data = [
        {
            "title": "Senior Data Engineer",
            "location": "Bangalore / Hybrid",
            "job_type": "Full-time",
            "description": "We are looking for an experienced Data Engineer to join our team. You will be responsible for expanding and optimizing our data and data pipeline architecture, as well as optimizing data flow and collection for cross functional teams.",
            "requirements": "5+ years of Python/SQL experience. Experience with Databricks and Spark."
        },
        {
            "title": "AI/ML Solutions Architect",
            "location": "Bangalore",
            "job_type": "Full-time",
            "description": "Design and implement machine learning applications and systems. You will be selecting the appropriate algorithms and tools, allowing us to generate accurate predictions and insights.",
            "requirements": "Strong background in Deep Learning, NLP, and Cloud AI services."
        },
        {
            "title": "Business Analyst - Healthcare",
            "location": "Remote",
            "job_type": "Contract",
            "description": "Bridge the gap between IT and the business using data analytics to assess processes, determine requirements and deliver data-driven recommendations.",
            "requirements": "Experience in Healthcare domain and commercially aware."
        }
    ]

    CareerJob.objects.all().delete()
    for job in jobs_data:
        CareerJob.objects.create(**job)
    print(f"Created {len(jobs_data)} jobs.")

    # 8. Blog Posts
    posts_data = [
        {
            "title": "The Future of AI in Healthcare",
            "content": "Artificial Intelligence is revolutionizing the healthcare industry. From predictive analytics to personalized medicine, AI is enabling doctors to make better decisions...",
            "author": "Dr. Anant R. Koppar"
        },
        {
            "title": "Optimizing Supply Chains with Big Data",
            "content": "In today's volatile market, supply chain visibility is key. Big Data analytics allows companies to predict disruptions and optimize routes in real-time...",
            "author": "Vishwanath Honnungar"
        },
        {
            "title": "Why Databricks for your Lakehouse?",
            "content": "The Lakehouse architecture combines the best elements of data lakes and data warehouses. Databricks provides a unified platform for data engineering, science, and analytics...",
            "author": "Pradeep N"
        }
    ]

    BlogPost.objects.all().delete()
    for post in posts_data:
        BlogPost.objects.create(**post)
    print(f"Created {len(posts_data)} blog posts.")

if __name__ == '__main__':
    populate()
