from rest_framework import serializers
from .models import (
    Banner, ServiceCategory, Industry, IndustrySection, CareerJob, 
    BlogPost, LeadershipMember, Partner, CompanyValue, 
    VisionMission, ContactMessage, SiteSetting
)

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'

class IndustrySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustrySection
        fields = '__all__'

class IndustrySerializer(serializers.ModelSerializer):
    sections = IndustrySectionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Industry
        fields = '__all__'

class CareerJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerJob
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class LeadershipMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadershipMember
        fields = '__all__'

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

class CompanyValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyValue
        fields = '__all__'

class VisionMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisionMission
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = '__all__'
