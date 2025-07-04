# news/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    MahallaViewSet, VillageViewSet, ElectricSupplyViewSet,
    WaterSupplyViewSet, EducationViewSet, HealthcareViewSet,
    PoliceNoticeViewSet, NewsViewSet, ContactViewSet,
    NewsListAPIView, DepartmentViewSet, GasSupplyListCreateView, GasSupplyDetailView,
    NewsDetailAPIView  # Yangi view qo‘shish
)

# 🔧 Router setup
router = DefaultRouter()
router.register(r'departments/mahalla', MahallaViewSet)
router.register(r'departments/village', VillageViewSet)
router.register(r'departments/electricity', ElectricSupplyViewSet)
router.register(r'departments/water', WaterSupplyViewSet)
router.register(r'departments/education', EducationViewSet)
router.register(r'departments/health', HealthcareViewSet)
router.register(r'departments/police', PoliceNoticeViewSet)
router.register(r'departments/news', NewsViewSet)
router.register(r'departments/contact', ContactViewSet)
router.register(r'departments', DepartmentViewSet)

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="News and Services API",
        default_version='v1',
        description="Mahalla, qishloq va xizmatlar haqida API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# 🔗 URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Router uchun asosiy yo‘l
    path('list/', NewsListAPIView.as_view(), name='news-list'),  # News list uchun
    path('departments/gas/', GasSupplyListCreateView.as_view()),
    path('departments/gas/<int:pk>/', GasSupplyDetailView.as_view()),
    path('departments/news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),  # Yangi detal yo‘li
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]