
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
        content="""
        <ul class="space-y-4">
            <li class="flex items-start">
                <span class="mr-2 text-brand-orange font-bold">•</span>
                <span>Enhance the quality of life by building world class products and solutions through innovative application of technology</span>
            </li>
            <li class="flex items-start">
                <span class="mr-2 text-brand-orange font-bold">•</span>
                <span>To become the most treasured business partner to all our customers with a customer-first philosophy</span>
            </li>
        </ul>
        """
    )
    VisionMission.objects.create(
        type='Vision', 
        content="""
        <ul class="space-y-4">
            <li class="flex items-start justify-end text-right">
                <span>To be a globally dominant platform based services company in the industry segments of our choice by 2025</span>
                <span class="ml-2 text-brand-purple font-bold">•</span>
            </li>
            <li class="flex items-start justify-end text-right">
                <span>Be a predominantly employee owned organization</span>
                <span class="ml-2 text-brand-purple font-bold">•</span>
            </li>
            <li class="flex items-start justify-end text-right">
                <span>Be a dream destination for every innovator to unleash their creativity by fostering a world class environment</span>
                <span class="ml-2 text-brand-purple font-bold">•</span>
            </li>
            <li class="flex items-start justify-end text-right">
                <span>To help companies make data driven business decisions</span>
                <span class="ml-2 text-brand-purple font-bold">•</span>
            </li>
        </ul>
        """
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
    # 5. Update Banners
    # Explicitly update HOME banners as per user request
    Banner.objects.filter(page='HOME').delete()
    
    home_banners = [
        {
            "title": "Intelligent Analytics & Digital Transformation",
            "subtitle": "For healthcare, automotive, logistics, pharma sectors."
        },
        {
            "title": "Rich Insights",
            "subtitle": "For optimal business decisions."
        },
        {
            "title": "Insight-Driven Culture",
            "subtitle": "Helping clients build a culture for better business."
        },
        {
            "title": "Efficiency & Cost Savings",
            "subtitle": "Data insights drive increased efficiency and cost savings."
        },
        {
            "title": "Better Client Experience",
            "subtitle": "Technology for enabling better client experience."
        }
    ]
    
    for b in home_banners:
        Banner.objects.create(
            page='HOME',
            title=b['title'],
            subtitle=b['subtitle'],
            image='banners/home_default.jpg', # Using default placeholder, component handles bg images
            active=True
        )

    # Explicitly update ABOUT banner to ensure new branding applies
    Banner.objects.filter(page='ABOUT').delete()

    # Ensure other page banners exist
    banner_configs = [
        ('ABOUT', '<span class="text-brand-purple">Kushagra</span><span class="text-brand-orange">mati Analytics</span>', 'A team of serial entrepreneurs and domain experts.'),
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
            "content": """Open CV is a huge open-source library for Computer Vision, Machine Learning and Image Processing. It focuses on image processing, video capture and analysis including face-detection and object detection. It can identify faces, objects or even the hand-writing of a human.

When it is integrated with NumPy (highly optimized library for numerical operations), whatever operations one can do in NumPy can be combined with OpenCV.

OpenCV supports a wide variety of programming languages such as C++, Python, Java etc. and is available on different platforms. It runs on both desktop (Windows, Linux, Android, MacOS, FreeBSD, OpenBSD) and mobile (Android, Maemo, iOS).
It is a cross-platform library.

# Computer Vision
Computer Vision is the way of teaching intelligence to machines and making them see things just like humans. In its simplest form, Computer Vision is what allows computer to see and process visual data just like humans. It involves analyzing images and videos to produce useful information.

# Applications:
A few of its applications are given below.
- Face Detection
- Cancer Detection
- COVID-19 diagnosis
- Movement Analysis
- Mask detection
- Traffic Flow Analysis
- Driver Attentiveness Detection
- Customer Tracking
- Theft Detection

Image processing is the most basic and one of the important concepts in Computer Vision. Just as we do data preprocessing techniques in Machine Learning to make our data ready for easy computation, images should also go through the same preprocessing techniques.

# Image Preprocessing:
In order to add a dataset of images to a convolutional network, all of the images should be of same size. Preprocessing includes image resizing, geometric and color transformations, gray-scale conversion, background removal, noise removal, edge detection and many more.

The acquired data is usually messy and come from different sources. To feed them to the ML model (or neural network), they need to be standardized and cleaned up. This can be done with the help of OpenCV. Preprocessing is used to conduct steps that reduce the complexity and increase the accuracy of the applied algorithm. We cannot write a unique algorithm for each of the condition in which an image is taken, thus, when we acquire an image, we convert it into a form that allows a general algorithm to solve it. This is the importance of image preprocessing.

Let’s take an example of an Image Classification problem.
Consider the image given below:
You can easily recognize it. It’s a car. When you were shown an image, you classified it to a class it belonged to (car, in this instance). This is what an image classification is all about. When you are given a dataset containing a massive number of images (say 10,000 or 1,00,000), manually checking and classifying is a tedious task. Here we have to build an image classification model.

Self-driving car is a great example where image classification is used in real world. To enable autonomous driving, we have to build an image classification model to recognize various objects like vehicles, people, obstacles, moving objects etc. on the road. So, the entire problem involves 4 steps;
1. Loading and preprocessing data
2. Defining model architecture
3. Training the model
4. Estimation of performance

Now, let us have a look at the role of OpenCV in Image Preprocessing techniques. This is used in cases when you want to analyze the images manually before feeding them into the training model.

1. Converting to Gray scale image
Gray-scale images reduces the complexity of computation as it removes all the unwanted information from the image.

2. Edge Detection
Canny edge detection is used to detect the edges in an image. It accepts a gray scale image as input and it uses a multistage algorithm which involves noise reduction, finding the edge gradient and direction, non-maximum suppression to remove any unwanted pixels which may not constitute the edge and Hysteresis thresholding to decide which all edges are really edges and which are not based on two threshold values ‘minVal’ and ‘maxVal’.

3. Noise Removal

4. Image Contouring

5. Blurring and Smoothing
It is done to find features or to remove noise from features. There are many methods available in OpenCV for performing blurring and smoothing. It includes:
- Gaussian Blurring
- Median Blurring
- Bilateral Blurring
- Gamma Correction
- Using built-in kernels
- Using user-defined kernels

6. Line Detection
This is done to detect the lines in images. For that, we use cv2.HoughLines(P) for doing that along with creating a mask through which we create the edges using Canny edge detector and then apply that output in the Hough line prediction function.

These are few of the image processing techniques which can be done using OpenCV. Other techniques include:
- Removing background from the image
- Color Detection
- Extracting text from image
- Rotate an image
- Adjust image contrast
- Crop an image
- Apply mask for colored image
- Centroid detection, etc.

Image processing allows a much wider range of algorithms to be applied to input data. The aim of image processing is to improve the image data (features) by suppressing unwanted distortions and enhancement of some important image features so that our training models can benefit from this improved data to work on which in turn improves the performance of the model.""",
            "author": "Neha V S",
            "image": "blog/opencv.jpg"
        },
        {
            "title": "Time Series Forecasting on COVID 19 using ARIMA",
            "content": """Time Series data is experimental data that has been observed at different points in time (usually evenly spaced, like once a day). For example, the data of airline ticket sales per day is a time series. However, just because a series of events has a time element does not automatically make it a time series, such as the dates of major airline disasters, which are randomly spaced and are not time series. These types of random processes are known as point process.

# Time Series Basics
Time Series have several key features such as trend, seasonality, and noise.

# Variation
One of the most important features of a time series is variation. Variations are patterns in the times series data. A time series that has patterns that repeat over known and fixed periods of time is said to have seasonality. Seasonality is a general term for variations that periodically repeat in data. In general, we think of variations as 4 categories: Seasonal, Cyclic, Trend, and Irregular fluctuations.

Seasonal variation is usually defined as variation that is annual in period, such as sweaters sales being higher in winter and lower in summer. Cyclic Variation is a variation that occurs at other fixed periods, such as the daily variation in temperature. Both Seasonal and Cyclic variation would be examples of seasonality in a time series data set.

Trends are long-term changes in the mean level, relative to the number of observations.

# Steps for ARIMA implementation
The general steps to implement an ARIMA model are:
- Load the data: The first step for model building is of course to load the dataset
- Preprocessing: Depending on the dataset, the steps of preprocessing will be defined. This will include creating timestamps, converting the dtype of date/time column, making the series univariate, etc.
- Make series stationary: In order to satisfy the assumption, it is necessary to make the series stationary. This would include checking the stationarity of the series and performing required transformations
- Determine d value: For making the series stationary, the number of times the difference operation was performed will be taken as the d value
- Determine the p and q values: Read the values of p and q using auto_arima model
- Fit ARIMA model: Using the processed data and parameter values we calculated from the previous steps, fit the ARIMA model
- Predict values on validation set: Predict the future values
- Calculate MAPE: To check the performance of the model, check the MAPE value using the predictions and actual values on the validation set

Let’s explore the COVID 19 Indian dataset statewise cases. 

Processing the Data
Pandas makes this easy, let’s quickly check the head of the data (the first 5 rows) to see what default format it comes in. Data contains statewise confirmed, recovered and death cases on daily basis count.

Converting the “Date_YMD” column into a proper timestamps format with the help of pandas. Setting up the “Date_YMD” as index, that way our forecasting analysis will be able to interpret these values.

We are predicting on daily basis, so resampling our data into Daily and taking the mean, which is similar to our original data. If we are predicting either weekly or monthly or yearly, then the mean value will change.

# Auto ARIMA
Usually, in the basic ARIMA model, we need to provide the p, d, and q values which are essential. We use statistical techniques to generate these values by performing the difference to eliminate the non-stationarity and plotting ACF and PACF graphs. In Auto ARIMA, the model itself will generate the optimal p, d, and q values which would be suitable for the data set to provide better forecasting.

Once fitting the whole dataset into auto_arima model, it will generate the best fit values of p, d and q which is suitable for our data.

Finalized the best model – ARIMA (5, 1, 2) – (p, d, q). Last 3 zeros (0, 0, 0) represents that, our data does not have any seasonality.

Using the above steps, we able to train and test our model for confirmed cases, death cases, cured cases, gender wise getting vaccination, brand wise vaccination (covaxin & covishield).""",
            "author": "Mohan Baabu",
            "image": "blog/timeseries.jpg"
        },
        {
            "title": "Social Media Analytics for National Security",
            "content": """Social media has evolved into an extremely powerful tool, not only for its users, but also for the public data it provides. In our digital age, social media intelligence is a critical component for keeping people and nations safe.

We know how open-source intelligence is moving up the priority list for intelligence professionals. Social media intelligence has emerged within the realm of open sources to support security initiatives. While social media sites are a valuable source of security information, they also present intelligence teams with a number of challenges

What exactly is social media intelligence, and how can intelligence teams effectively use it in today's information environment?

What is Social Media Intelligence?
Social Media Intelligence is the process of collecting and analyzing social media data to gain meaningful insights, usually using specialized tools and methodologies, known as social media intelligence. The term "social media monitoring" is also used to describe the general practice of gathering and analyzing public social media activity, though not always in the context of intelligence. "Social listening" refers to the collection of larger data sets in order to extract general trends and insights, and it is frequently used in commercial and marketing applications

Why is Social Media Intelligence Valuable for National security?
SOCMINT is useful in national security for a variety of reasons. The spread of social media provides analysts with a wealth of security information that would otherwise be unavailable via other channels, such as classified INTs.

Social media intelligence also sheds light on broader trends in a specific information environment. This provides more comprehensive insights, especially when other intelligence types concentrate on specific targets rather than broad populations.

How do Social Media Intelligence Tools Address These Challenges?
In a country like India, Internal security forces are becoming overburdened as a result of armed struggle and separatist calls from across the country.
- Provoking statements made in the news media
- Increase in divisive propaganda on social media
- Unusual funds transfer from foreign countries
- Unusual pattern of cash withdrawal
- Rapid increase in SIM card sales
- Changes in an area's demographic pattern
- An area's economic activity
- Face recognition using video analytics

Details of all of the activities listed above are available in the public domain. The problem is that this is unstructured data, which makes it difficult to generate appropriate analytical insights.

This is where modern big data analytics platforms, such as Databricks, come in. These platforms can ingest information from thousands of streams of data in a variety of formats.

The majority of the data for ingesting can be obtained from the service providers themselves as a statutory requirement.

As more data is ingested, the data that drives the Social Analytics Dashboard and the Occurrence Predictability Model can be refined to improve accuracy.

Social Media Intelligence is a newer intelligence discipline in the government. Emerging technologies assist in addressing common challenges associated with large-scale leveraging of public social data, such as data overload, information gaps and data privacy.

Hope this blog is informative and interesting and we are taking these steps on a journey that benefits all of us.""",
            "author": "Genevive Gloria Mendonca",
            "image": "blog/socialmedia.jpg"
        },
        {
            "title": "Graph Database: Wave of the future in documenting Data",
            "content": """In Today’s world, Customers' demand for immediate access to services and money transfers creates chances for criminals. For instance, payment service apps work to send money as soon as possible to legitimate users while simultaneously ensuring that it isn't transmitted for illegal purposes or used to conceal the genuine recipient by taking devious ways. This necessitates real-time fraud detection. Graphs increase access to data and allow for lightning-fast response times to queries, graphs have gained popularity as a solution for real-time fraud detection.

Not just the transactions themselves can be modeled in graphs when analyzing transactions with graph technology. Due to the tremendous flexibility of graphs, it is possible to model the varied surrounding information. For example, the connections between client IP addresses, ATM geolocation, card numbers, and account IDs can all become vertices. The rules for identifying fraud can be designed by users based on datasets in online banking and ATM location research.

Detection rules can be setup for:
- IPs that sign in using several cards that are registered in various locations
- Cards used across numerous locations at great distances
- Accounts receiving one-time inbound transactions from other accounts registered in various places

In the modern world, Companies are aware of the need to innovate or risk being disrupted. Using a graph database, you can see the data landscape quite differently. It helps to Gain new knowledge, resolve difficult issues, and unlock countless opportunities

A customized, single-purpose platform for building and modifying graphs is referred to as a graph database. Graphs contain nodes, edges, and properties, all of which are used to represent and store data in a way that relational databases are not equipped to do. Data is saved in a manner akin to how thoughts could be scribbled on a whiteboard. Your data is kept in a way that doesn't limit it to a pre-established model, enabling very flexible thinking and usage.

How Graphs and Graph Database work
For displaying data relationships, graphs and graph databases offer graph models. They enable "traversal queries" based on connections and use graph algorithms to find patterns, paths, communities, influencers, single points of failure, and other relationships, allowing for more effective analysis at scale against enormous amounts of data. The power of graphs is in analytics, the insights they provide, and their ability to link disparate data sources. Algorithms investigate the paths and distance between the vertices, their significance, and the clustering of the vertices when studying graphs. For instance, algorithms will frequently consider the relevance of nearby vertices, incoming edges, and other indicators when determining importance.

Understanding things that are challenging to see with other techniques is made feasible by graph algorithms, operations specifically designed to evaluate linkages and behaviours among data in graphs. Algorithms investigate the pathways and separation between the vertices, their significance, and the clustering of the vertices when studying graphs. In order to determine relevance, the algorithms frequently consider incoming edges, the significance of nearby vertices, and other signs. For example, Graph algorithms can determine which person or thing is more related to others in social networks or commercial procedures. The algorithms will often look at incoming edges, importance of neighboring vertices, and other indicators to help determine importance

Advantages of Graph databases
When looking for distant relationships or analysing data based on factors like relationship strength or quality, the graph format offers a more versatile platform. For a variety of corporate use cases, such as fraud detection in banking, detecting connections in social networks, and customer 360, graphs enable you to explore and uncover connections and patterns in social networks, IoT, big data, data warehouses, as well as complex transaction data. To make links in relationships more understandable, graph databases are now being used more and more in data science.

The image provides a visual representation of the well- known party game "Six Degrees of Kevin Bacon," which challenges players to identify connections between Kevin Bacon and other actors based on a series of mutual films. It is the best technique to illustrate graph analytics since it places a strong emphasis on relationships. Imagine a data set with two categories of nodes: every film ever made and every actor that has been in those films. Then, using graphs, we run a query asking to connect Kevin Bacon to Muppet icon Miss Piggy. In this example, the available nodes (vertices) are both actors and films and the relationships (edges) are the status of “acted in.” From this we can find that Kevin Bacon acted in The River Wild with Meryl Streep.  Meryl Streep acted in Lemony Snicket’s A Series of Unfortunate Events with Billy Connolly and also, Billy Connolly acted in Muppet Treasure Island with Miss Piggy.

Graph database use cases
The areas listed below are just a few where Graph Database can be effectively used:
- Near-real-time retail trend analysis
- Fraud / Crime detection by identifying anti-patterns
- Database-driven workflows in Robotic Process Automation
- Alternate route identification in Logistics
- Production Planning in Manufacturing
- Customer profiling & product cross-Selling

The future of graph databases""",
            "author": "Panchami V T",
            "image": "blog/graphdb.jpg"
        },
        {
            "title": "Let’s Discover the EC2 Service from Amazon Web Services (AWS)",
            "content": """Kushagramati Analytics was where I started in the vast world of data. The training opportunities provided by this job have been extraordinary to say the least, and the freedom to learn has been extremely encouraging. I began by learning Python, Pandas and NumPy, followed by numerous courses in Databricks and Boomi Integration, and then moved on to the Cloud platform.

Cloud computing is like a bus. You didn’t have to buy, maintain, or operate the vehicle, yet somehow you can still use it to get around and pay only for your trip. The cloud is like that, you don’t have to buy, maintain, or operate servers, you just pay for running your website or web service on them, and leave the maintenance and operations to someone else to deal with.

So, what does the cloud look like to someone using it? A lot of people are unaware that Amazon, in addition to being the most well-known online retailer, is also one of the top suppliers of cloud computing services i.e., Amazon Web Services.

AWS is the world's most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centres globally. Google is another major cloud provider which is called Google cloud computing, we also have another player from Microsoft called Microsoft Azure Cloud Computing Platform & Services and IBM’s IBM Cloud. The list goes on. As you can see, cloud services are big business today; some of the tech industry giants are in on the game.

Let’s peek behind the scenes at what it looks like to be using the cloud. When we log into AWS, here is what we see:

This is a list of pretty much ALL the cloud services that AWS provides. A lot of them have very specific purposes, and most applications only need to use a fraction of these services. The reason there are so many is because the cloud industry has moved forward from just providing a “server” that looks and feels just like one you might set up yourself (known as “Platform as a Service”), to providing access to just the actual software you’d run, so you no longer have to even deal with installation, configuration, and upgrading (known as “Software as a Service”).""",
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
