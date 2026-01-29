from rest_framework import viewsets, mixins, permissions
from .models import (
    Banner, ServiceCategory, Industry, CareerJob, 
    BlogPost, LeadershipMember, Partner, CompanyValue, 
    VisionMission, ContactMessage, SiteSetting, Tool, CaseStudy
)
from .serializers import (
    BannerSerializer, ServiceCategorySerializer, IndustrySerializer, 
    CareerJobSerializer, BlogPostSerializer, LeadershipMemberSerializer, 
    PartnerSerializer, CompanyValueSerializer, VisionMissionSerializer, 
    ContactMessageSerializer, SiteSettingSerializer, ToolSerializer, CaseStudySerializer
)

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.filter(active=True)
    serializer_class = BannerSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        page = self.request.query_params.get('page')
        if page:
            queryset = queryset.filter(page=page)
        return queryset
    permission_classes = [permissions.AllowAny]

class ServiceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [permissions.AllowAny]

class IndustryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

class CareerJobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CareerJob.objects.filter(active=True)
    serializer_class = CareerJobSerializer
    permission_classes = [permissions.AllowAny]

class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.filter(active=True)
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

class LeadershipMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LeadershipMember.objects.all()
    serializer_class = LeadershipMemberSerializer
    permission_classes = [permissions.AllowAny]

class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.AllowAny]

class CompanyValueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CompanyValue.objects.all()
    serializer_class = CompanyValueSerializer
    permission_classes = [permissions.AllowAny]

class VisionMissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VisionMission.objects.all()
    serializer_class = VisionMissionSerializer
    permission_classes = [permissions.AllowAny]

class SiteSettingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SiteSetting.objects.all()
    serializer_class = SiteSettingSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        # Always return the first object or None
        return SiteSetting.objects.first()

    def list(self, request, *args, **kwargs):
        # Override list to return just the object if desired, or let it return list [obj]
        # For simplicity, returning list.
        return super().list(request, *args, **kwargs)


class ContactMessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Here we can add email sending logic later
        serializer.save()

class ToolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    permission_classes = [permissions.AllowAny]

class CaseStudyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    permission_classes = [permissions.AllowAny]

