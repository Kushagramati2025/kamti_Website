
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import ServiceCategory, LeadershipMember, VisionMission, SiteSetting, Banner, Industry, IndustrySection

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

    # 1.5 Real Industry Solutions (Detailed)
    Industry.objects.all().delete()
    
    # Healthcare Data
    healthcare = Industry.objects.create(
        name="Healthcare",
        description="Solutions for Healthcare sector.",
        banner_image="industries/banners/healthcare_banner.jpg" 
    )

    # Healthcare Sections
    healthcare_sections = [
        {
            "title": "Data insights drive increased efficiency cost savings",
            "content": "Increased prevalence of lifestyle disorders creating a huge demand of accessible healthcare systems. The healthcare market is being propelled with technological advancements with rising in healthcare costs & transparency. The biggest obstacles today comes up with handling huge volume of meta data to extract the significant information & providing superior customer experience.",
            "image": "industries/sections/data_insights.jpg"
        },
        {
            "title": "Predictive disease analysis",
            "content": "When it comes to predicting future health outcomes, big data analysis is critical. As a result, there is a lot of research being done on predictive analytics and machine learning approaches to reveal improved decision making. Big data analysis opens up new avenues for predicting future health state based on health metrics and delivering the best results.",
            "image": "industries/sections/predictive_analysis.jpg"
        },
        {
            "title": "Intelligent chatbot using AI/NLP",
            "content": "In the field of healthcare, maintaining a healthy lifestyle is crucial. It might be difficult to locate a doctor's consultation for health difficulties in some less-socialized places. The fundamental aim is to create a healthcare chatbot based on Artificial Intelligence and Natural Language Processing (NLP) that can identify a problem and offer necessary facts about it before consulting or visiting a doctor.",
            "image": "industries/sections/ai_chatbot.jpg"
        },
        {
            "title": "Reduce Healthcare costs with benefits and recommendations",
            "content": "Advanced machine learning models, suitable laboratory equipment, machine learning, and data science, which assist in creating medicines to improve patients' fast treatment at a lower cost, can help identify between cancers and healthy anatomy with 3D radiological images to enable medical experts in radiation therapy and surgical planning.",
            "image": "industries/sections/cost_reduction.jpg"
        },
        {
            "title": "Optima x-ray predictor",
            "content": "Case Study: Identifying between cancers and healthy anatomy with 3D radiological images to enable medical experts.<br><br><a href='#' class='btn-primary'>Download Case Study</a>",
            "image": "industries/sections/xray.jpg"
        }
    ]

    for section in healthcare_sections:
        IndustrySection.objects.create(industry=healthcare, **section)

    # Automotive Data
    automotive = Industry.objects.create(
        name="Automotive",
        description="Empowering Automakers with Next-Gen Technologies. The global automotive industry is undergoing a tremendous amount of change at an unprecedented pace. The experience of electric vehicles (EV) and autonomous vehicles (AV) is being enhanced by technological advancements, including multi-sensor, AI-enabled, over-the-air upgrades, and more. Especially with generative AI, the automotive sector has countless possibilities, from voice and virtual assistants to material and generative design.",
        banner_image="industries/banners/automotive_banner.jpg"
    )

    automotive_sections = [
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

    for section in automotive_sections:
        IndustrySection.objects.create(industry=automotive, **section)

    # Logistics Data
    logistics = Industry.objects.create(
        name="Logistics",
        description="Helping clients build an insight-driven culture for better business. The rapid evolution in the logistics sector has streamlined Operations & Efficiency, but at the same time, the digital age has impacted majorly on the industry. The effects can be seen in Customer Experience, Digitalization of Transactions, and Technology Adaption with respect to the transaction volume and the Evermore demanding consumers. Thereby enormous flow of goods will generate a huge amount of data that can be harnessed using Intelligent Analytics.",
        banner_image="industries/banners/logistics_banner.jpg" 
    )

    logistics_sections = [
        {
            "title": "Last Mile Delivery",
            "content": "Last-mile delivery is one of the most challenging components of the whole shipping process, despite being one of the most important variables in customer satisfaction. Processing of data collected from GPS helps build a system at its core. Optimizing the route with telematics databases can be tapped to automatically adjust the routes based on real-time data of the latest order, Routing, Address identification for ease of delivery.",
            "image": "industries/sections/logistics_last_mile.jpg"
        },
        {
            "title": "Warehouse surveillance – Video Analytics",
            "content": "Securing warehouses from both external and Internal threats/thefts has been a critical challenge with the increase in the trading of goods. It is a critical decision to make sure the valuables are well protected from break-Ins in a commercial space which can now be enabled using smart video analytics application.",
            "image": "industries/sections/logistics_warehouse.jpg"
        },
        {
            "title": "Demand Forecasting",
            "content": "To anticipate future events using data analytics, the data sources and datasets are used with the combination of machine learning algorithms to discover patterns, demand signals, and spot intricate relationships. AI-powered forecasting models can cut errors by 30 to 50 percent with the increased accuracy resulting in a 65 percent reduction in missed sales.",
            "image": "industries/sections/logistics_forecasting.jpg"
        },
        {
            "title": "Sentiment analysis",
            "content": "Classification of text based on keywords.<br><br><a href='#' class='btn-primary'>Download Case Study</a>",
            "image": "industries/sections/logistics_sentiment.jpg"
        }
    ]

    for section in logistics_sections:
        IndustrySection.objects.create(industry=logistics, **section)

    # Pharma Data
    pharma = Industry.objects.create(
        name="Pharma",
        description="Technology for enabling better client experience. The pharmaceutical landscape has made a progress in the field of precision medicines has opened up numerous possibilities to target different health maladies out of which major focus for precision health, rare genetic disorders, mutation spectrum of genetic and complex diseases which makes an array of opportunities for personalized medicine. The current challenges of having semi-structured data to develop breakthrough therapies is still stagnant.",
        banner_image="industries/banners/pharma_banner.jpg" 
    )

    pharma_sections = [
        {
            "title": "Data Lake Preparation for Genomic Data",
            "content": "Practical challenges with genomic datasets containing semi-structured records layering with respect to its size & complexity while uncertainty in the interpretation of regulatory requirements for return of results. Data from Medical Devices, Medical Records, Images and Insurance claims (Stage-1).",
            "image": "industries/sections/pharma_data_lake.jpg"
        },
        {
            "title": "Developing models to show correlation between Genomic data",
            "content": "The variation being less than 1% while comparing a healthy person Genome with a person having Genetic disorder as its needs a huge computation/processing to find the sequence of records to discover the variation patterns. Developing models to show correlation between Genomic data and other set of data to provide greater insights into research findings (Stage-2).",
            "image": "industries/sections/pharma_models.jpg"
        },
        {
            "title": "Genomic Data Analysis for faster Drug Discovery",
            "content": "Genomic sequence can be Patient data analysis which can be performed combining the stage 1 records and stage 2 insights which helps for a drug discovery, Advance Personalization in healthcare & predict the hereditary diseases.",
            "image": "industries/sections/pharma_drug_discovery.jpg"
        },
        {
            "title": "Recommend next best steps for sales",
            "content": "The competitive landscape market for the Genomic insights & bioinformatics progression will boost the companies to excel their Diagnostics & Research Advancements resulting the spike in growth trajectory to Novel Pharma discoveries & Genetic solutions.",
            "image": "industries/sections/pharma_sales.jpg"
        }
    ]

    for section in pharma_sections:
        IndustrySection.objects.create(industry=pharma, **section)

    print(f"Created and populated Healthcare, Automotive, Logistics, and Pharma industries.")

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
