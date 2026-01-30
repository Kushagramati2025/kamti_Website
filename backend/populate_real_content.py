
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
        description="Increased prevalence of lifestyle disorders creating a huge demand of accessible healthcare systems. The healthcare market is being propelled with technological advancements with rising in healthcare costs & transparency. The biggest obstacles today comes up with handling huge volume of meta data to extract the significant information & providing superior customer experience",
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
            "content": "Case Study: Identifying between cancers and healthy anatomy with 3D radiological images to enable medical experts.<br><br><a href='http://127.0.0.1:8000/media/casestudies/pdfs/Optima_XRay_Predictor.pdf' target='_blank' class='btn-primary inline-flex items-center px-6 py-3 border border-transparent text-base font-bold rounded-lg text-white bg-brand-orange hover:bg-brand-orange-dark shadow-md transition-all duration-300'>Download Case Study</a>",
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
            "content": "Classification of text based on keywords.<br><br><a href='http://127.0.0.1:8000/media/casestudies/pdfs/Sentiment_Analysis.pdf' target='_blank' class='btn-primary inline-flex items-center px-6 py-3 border border-transparent text-base font-bold rounded-lg text-white bg-brand-orange hover:bg-brand-orange-dark shadow-md transition-all duration-300'>Download Case Study</a>",
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
            "position": "Chief Executive Officer and Managing Director",
            "bio": "Dr. Anant R Koppar drives business strategy and relationships in Kushagramati Analytics. He was the Founder President of Kshema Technologies, one of India's first venture capital-funded software services companies. He worked as the President of the Technologies Division of MphasiS BFL Limited post the acquisition of Kshema by MphasiS. A certified 'Project Management Professional' by PMI, Anant Koppar was the first CEO in India to get this certification. His last venture was KTwo Technology Solutions. He is a recognized leader in the software industry and has been awarded the highest civilian award “Karnataka Rajyotsava“ by the Karnataka Government for outstanding contributions to the growth of the IT Industry in Karnataka, India.",
            "image": "leadership/dr_anant.png"
        },
        {
            "name": "Vishwanath Honnungar",
            "position": "Chief Technology Officer",
            "bio": "With 30 years of experience in the IT services industry, Vishwanath brings strategic insight to Kushagramati’s leadership team, and deep operational knowledge of driving business growth, furthering partnerships, and leading cross-cultural teams. In his role he will be responsible for focus on strategy, business development, account management and digital transformation solutions, with a special focus on Data Analytics services, to leverage the company’s strengths in cognitive solutions. He has in-depth global experience in the services industry with an outstanding track record in leading and growing small and large business units. Vishwanth brings in extensive knowledge and experience in architecture, design, development methodologies, testing, and quality processes.",
            "image": "leadership/vishwanath.jpg"
        },
        {
            "name": "Pradeep N",
            "position": "Industry Expert and Operations",
            "bio": "With 6 years in Manufacturing and 30 years in IT services industry, Pradeep brings in a rich domain experience in the process automation of Manufacturing, Healthcare, Financial Services and Logistics. In his previous organizations, he has brought about improvement in operational efficiency, closer integration of various departments and businesses, risk management and operational cost effectiveness. His specialization is in Digital Transformation, Program Management, Delivery Management and Process re-engineering. In his role, he is responsible for scoping, delivering, and successfully closing projects, managing and accelerating account growth, augment revenue with existing & prospective clients. On the technology front, he is exposed to Big Data Analytics, Master Data Management for Business 360 view and on using Automation Tools in all stages of Software Design, Development and Testing.",
            "image": "leadership/pradeep.jpg"
        },
        {
             "name": "Dayanand Yardi",
             "position": "Finance and Administration",
             "bio": "As an established finance leader for 30 plus years’, Dayanand has extensive global leadership experience including shareholder value creation, mergers and acquisitions, financial and strategic planning, and budgeting. He has vast experience in managing finance and account functions in corporate as well as public sector companies. In his role at Kushagramti, Dayanand is responsible for the finance function which includes Corporate Finance, Business Finance, Business Planning, Treasury, Taxation, and Investor relations.",
             "image": "leadership/dayanand.png"
        },
        {
             "name": "Shruthi Malagi",
             "position": "Business Development",
             "bio": "Shruthi Malagi is an astute & result oriented Bid management professional with more than a decade of experience working in a leading IT services company. Her career growth has been in IT & ITES in strategic Business Development, Pre-sales and complex Bid Management across industries and geographies. With strong passion towards business development, she drives company operations, human resources and manages vendor relations.",
             "image": "leadership/shruthi.png"
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

    # 3.5. Company Values
    from core.models import CompanyValue
    values_data = [
        {
            "title": "Freedom to Innovate",
            "description": "We believe in giving our team the freedom to explore new ideas and innovate without boundaries.",
            "icon": "lightbulb" 
        },
        {
            "title": "Tolerance for Failure",
            "description": "Adopting the concept of 'fast fail' - we see failure as a stepping stone to success and learning.",
            "icon": "refresh"
        },
        {
            "title": "Individual Brilliance in Team Play",
            "description": "We recognize and celebrate individual brilliance, but always within the context of supportive team play.",
            "icon": "users"
        },
        {
            "title": "Mutually Beneficial Relationships",
            "description": "Building value-based, mutually beneficial relationships with all our stakeholders is at our core.",
            "icon": "handshake"
        },
        {
            "title": "Ethical Business Practices",
            "description": "We uphold the highest order of ethical business practices in everything we do.",
            "icon": "scale"
        }
    ]

    CompanyValue.objects.all().delete()
    for val in values_data:
        # Note: Icon field expects an image, but we might want to store a class name or use a default.
        # For now, we will create the object. If icon is ImageField, we might skip it or use a placeholder if required.
        # The model definition: icon = models.ImageField(upload_to='values/', blank=True, null=True)
        # So we can skip it.
        CompanyValue.objects.create(title=val['title'], description=val['description'])
    print(f"Created {len(values_data)} company values.")

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
        ('ABOUT', 'About Kushagramati', 'A team of serial entrepreneurs and domain experts.'),
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
        {"name": "Databricks", "website": "https://databricks.com", "logo": "partners/databricks_Logo.avif"},
        {"name": "Databricks Consulting Partner", "website": "https://databricks.com/partners", "logo": "partners/databricks_badge_v2.avif"},
        {"name": "Vue.ai", "website": "https://vue.ai", "logo": "partners/Picture3.avif"},
        {"name": "Boomi", "website": "https://boomi.com", "logo": "partners/boomi_v2.avif"},
        {"name": "Computomic", "website": "https://computomic.com", "logo": "partners/Computomic-Logo.avif"},
        {"name": "Snowflake", "website": "https://www.snowflake.com", "logo": "partners/snowflake.avif"},
        {"name": "Microsoft Azure", "website": "https://azure.microsoft.com", "logo": "partners/Microsoft.avif"},
        {"name": "AWS", "website": "https://aws.amazon.com", "logo": "partners/aws.avif"},
        {"name": "MSME", "website": "https://msme.gov.in", "logo": "partners/msme.avif"},
    ]
    
    # Check if Partner model exists imported (it wasn't in top import, adding it)
    from core.models import Partner, CareerJob, BlogPost

    Partner.objects.all().delete()
    for p in partners_data:
        Partner.objects.create(name=p['name'], website=p['website'], logo=p['logo'])
    print(f"Created {len(partners_data)} partners.")

    # 7. Departments & Careers
    from core.models import Department, PageSection
    
    # Create Departments
    Department.objects.all().delete()
    eng_dept = Department.objects.create(name="Engineering")
    sales_dept = Department.objects.create(name="Sales & Marketing")
    product_dept = Department.objects.create(name="Product Management")
    consulting_dept = Department.objects.create(name="Consulting")
    
    print("Created Departments.")

    # Create Page Section Config
    PageSection.objects.all().delete()
    PageSection.objects.create(
        page="CAREERS",
        section_key="OPEN_POSITIONS",
        title="Open Positions",
        subtitle="Ready to make an impact? Check out our current openings."
    )
    print("Created Page Section configs.")

    jobs_data = [
        {
            "title": "Senior Data Engineer",
            "department": eng_dept,
            "location": "Bangalore / Hybrid",
            "job_type": "Full-time",
            "is_remote": True,
            "salary_range": "$30k - $50k",
            "description": "We are looking for an experienced Data Engineer to join our team. You will be responsible for expanding and optimizing our data and data pipeline architecture, as well as optimizing data flow and collection for cross functional teams.",
            "requirements": "5+ years of Python/SQL experience. Experience with Databricks and Spark."
        },
        {
            "title": "AI/ML Solutions Architect",
            "department": eng_dept,
            "location": "Bangalore",
            "job_type": "Full-time",
            "is_remote": False,
            "salary_range": "$40k - $70k",
            "description": "Design and implement machine learning applications and systems. You will be selecting the appropriate algorithms and tools, allowing us to generate accurate predictions and insights.",
            "requirements": "Strong background in Deep Learning, NLP, and Cloud AI services."
        },
        {
            "title": "Business Analyst - Healthcare",
            "department": consulting_dept,
            "location": "Remote",
            "job_type": "Contract",
            "is_remote": True,
            "salary_range": "$20k - $40k",
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
            "title": "Role of OpenCV in Image Preprocessing",
            "content": "Open CV is a huge open-source library for Computer Vision, Machine Learning and Image Processing. It focuses on image processing, video capture and analysis including face-detection and object detection. It can identify faces, objects or even the hand-writing of a human.",
            "author": "Neha V S",
            "image": "blog/opencv.jpg"
        },
        {
            "title": "Time Series Forecasting on COVID 19 using ARIMA",
            "content": "Time Series data is experimental data that has been observed at different points in time (usually evenly spaced, like once a day). For example, the data of airline ticket sales per day is a time series. However, just because a series of events has a time element does not automatically make it a time series, such as the dates of major airline disasters, which are randomly spaced and are not time series. These types of random processes are known as point process.",
            "author": "Mohan Baabu",
            "image": "blog/timeseries.jpg"
        },
        {
            "title": "Social Media Analytics for National Security",
            "content": "Social media has evolved into an extremely powerful tool, not only for its users, but also for the public data it provides. In our digital age, social media intelligence is a critical component for keeping people and nations safe.",
            "author": "Genevive g",
            "image": "blog/socialmedia.jpg"
        },
        {
            "title": "Graph Database: Wave of the future in documenting Data",
            "content": "In Today’s world, Customers' demand for immediate access to services and money transfers creates chances for criminals. For instance, payment service apps work to send money as soon as possible to legitimate users while simultaneously ensuring that it isn't transmitted for illegal purposes or used to conceal the genuine recipient by taking devious ways. This necessitates real-time fraud detection. Graphs increase access to data and allow for lightning-fast response times to queries, graphs have gained popularity as a solution for real-time fraud detection.",
            "author": "Panchami V T",
            "image": "blog/graphdb.jpg"
        },
        {
            "title": "Let’s Discover the EC2 Service from Amazon Web Services (AWS)",
            "content": "Kushagramati Analytics was where I started in the vast world of data. The training opportunities provided by this job have been extraordinary to say the least, and the freedom to learn has been extremely encouraging. I began by learning Python, Pandas and NumPy, followed by numerous courses in Databricks and Boomi Integration, and then moved on to the Cloud platform.",
            "author": "Syeda Arfa",
            "image": "blog/aws_ec2.jpg"
        }
    ]

    BlogPost.objects.all().delete()
    for post in posts_data:
        BlogPost.objects.create(**post)
    print(f"Created {len(posts_data)} blog posts.")

if __name__ == '__main__':
    populate()
