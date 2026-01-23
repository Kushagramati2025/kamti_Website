from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BannerViewSet, ServiceCategoryViewSet, IndustryViewSet, 
    CareerJobViewSet, BlogPostViewSet, LeadershipMemberViewSet, 
    PartnerViewSet, CompanyValueViewSet, VisionMissionViewSet, 
    ContactMessageViewSet, SiteSettingViewSet
)

router = DefaultRouter()
router.register(r'banners', BannerViewSet)
router.register(r'services', ServiceCategoryViewSet)
router.register(r'industries', IndustryViewSet)
router.register(r'careers', CareerJobViewSet)
router.register(r'blog', BlogPostViewSet)
router.register(r'leadership', LeadershipMemberViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'values', CompanyValueViewSet)
router.register(r'vision-mission', VisionMissionViewSet)
router.register(r'contact', ContactMessageViewSet)
router.register(r'settings', SiteSettingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
