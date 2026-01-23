from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import (
    Banner, ServiceCategory, Industry, CareerJob, BlogPost, 
    LeadershipMember, Partner, CompanyValue, VisionMission, SiteSetting
)
from django.core.files.base import ContentFile
import base64

# Minimal 1x1 pixel gif as dummy image
DUMMY_IMG_DATA = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'

class Command(BaseCommand):
    help = 'Seeds database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            self.stdout.write('Superuser created: admin/admin')

        # Site Settings
        if not SiteSetting.objects.exists():
            SiteSetting.objects.create(
                site_name="KMATI",
                contact_email="info@kmati.in",
                contact_phone="+91 1234567890",
                address="123 Tech Park, India",
                facebook_url="https://facebook.com",
                linkedin_url="https://linkedin.com"
            )
            self.stdout.write('Site Settings created')

        # Banners
        if not Banner.objects.exists():
            b1 = Banner(
                title="Intelligent Analytics & Digital Transformation", 
                subtitle="For Healthcare, Automotive, Logistics, Pharma Sectors", 
                active=True, 
                order=1
            )
            b1.image.save('banner1.gif', ContentFile(DUMMY_IMG_DATA))
            b1.save()
            
            b2 = Banner(
                title="Innovation Leaders", 
                subtitle="We are ISO 9001:2015 certified company", 
                active=True, 
                order=2
            )
            b2.image.save('banner2.gif', ContentFile(DUMMY_IMG_DATA))
            b2.save()
            self.stdout.write('Banners created')

        # Services
        if not ServiceCategory.objects.exists():
            services = ['IT Consulting', 'Cloud Solutions', 'Data Analytics', 'Cyber Security']
            for s in services:
                obj = ServiceCategory(name=s, description=f"Comprehensive {s} services.")
                obj.save() # No icon for now
            self.stdout.write('Services created')

        # Industries
        if not Industry.objects.exists():
            industries = ['Healthcare', 'Automotive', 'Logistics', 'Pharma']
            for i in industries:
                obj = Industry(name=i, description=f"Solutions for {i} sector.")
                obj.banner_image.save(f'{i}_banner.gif', ContentFile(DUMMY_IMG_DATA))
                obj.save()
            self.stdout.write('Industries created')

        # Careers
        if not CareerJob.objects.exists():
            CareerJob.objects.create(
                title="Senior Python Developer",
                location="Remote",
                job_type="Full-time",
                description="Looking for Django expert.",
                requirements="Python, Django, DRF, Docker"
            )
            CareerJob.objects.create(
                title="Angular Frontend Engineer",
                location="Bangalore",
                job_type="Full-time",
                description="Build modern UIs.",
                requirements="Angular 17, Tailwind, TypeScript"
            )
            self.stdout.write('Careers created')

        # Blog
        if not BlogPost.objects.exists():
            b = BlogPost(
                title="Future of AI in Industry",
                content="AI is transforming everything...",
                author="John Doe"
            )
            b.image.save('blog1.gif', ContentFile(DUMMY_IMG_DATA))
            b.save()
            self.stdout.write('Blog created')

        # Leadership
        if not LeadershipMember.objects.exists():
            l = LeadershipMember(name="Jane Doe", position="CEO", bio="Visionary leader")
            l.image.save('ceo.gif', ContentFile(DUMMY_IMG_DATA))
            l.save()
            self.stdout.write('Leadership created')

        # Partners
        if not Partner.objects.exists():
            p = Partner(name="Tech Corp", website="https://example.com")
            p.logo.save('partner1.gif', ContentFile(DUMMY_IMG_DATA))
            p.save()
            self.stdout.write('Partners created')

        # Values
        if not CompanyValue.objects.exists():
            CompanyValue.objects.create(title="Integrity", description="We do the right thing.")
            CompanyValue.objects.create(title="Innovation", description="We create the future.")
            self.stdout.write('Values created')

        # Vision/Mission
        if not VisionMission.objects.exists():
            VisionMission.objects.create(type="Vision", content="To be the global leader in tech.")
            VisionMission.objects.create(type="Mission", content=" delivering excellence every day.")
            self.stdout.write('Vision/Mission created')

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
