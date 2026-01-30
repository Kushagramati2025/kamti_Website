from django.contrib import admin
from .models import (
    Banner, ServiceCategory, Industry, IndustrySection, 
    CareerJob, BlogPost, LeadershipMember, Partner, 
    CompanyValue, VisionMission, ContactMessage, SiteSetting,
    PageSection, Department, Tool, CaseStudy
)

# Custom Admin Classes

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'active', 'order')
    list_filter = ('page', 'active')
    search_fields = ('title', 'subtitle')

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order')
    prepopulated_fields = {'slug': ('name',)}

class IndustrySectionInline(admin.StackedInline):
    model = IndustrySection
    extra = 1

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [IndustrySectionInline]

@admin.register(CareerJob)
class CareerJobAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'location', 'job_type', 'is_remote', 'posted_date', 'active')
    list_filter = ('active', 'job_type', 'is_remote', 'department')
    search_fields = ('title', 'description', 'requirements')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(LeadershipMember)
class LeadershipMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'order')

@admin.register(CompanyValue)
class CompanyValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

@admin.register(VisionMission)
class VisionMissionAdmin(admin.ModelAdmin):
    list_display = ('type',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message', 'attachment', 'created_at')
    readonly_fields = ('created_at',)
    search_fields = ('name', 'email', 'phone', 'subject', 'message')

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True

@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ('page', 'section_key', 'title', 'active')
    list_filter = ('page', 'active')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
