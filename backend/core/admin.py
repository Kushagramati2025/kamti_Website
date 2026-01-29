from django.contrib import admin
from .models import (
    Banner, ServiceCategory, Industry, IndustrySection, 
    CareerJob, BlogPost, LeadershipMember, Partner, 
    CompanyValue, VisionMission, ContactMessage, SiteSetting,
    Tool, CaseStudy
)

# Register your models here.
admin.site.register(Banner)
admin.site.register(ServiceCategory)
admin.site.register(Industry)
admin.site.register(IndustrySection)
admin.site.register(CareerJob)
admin.site.register(BlogPost)
admin.site.register(LeadershipMember)
admin.site.register(Partner)
admin.site.register(CompanyValue)
admin.site.register(VisionMission)
admin.site.register(ContactMessage)
admin.site.register(SiteSetting)
admin.site.register(Tool)
admin.site.register(CaseStudy)
