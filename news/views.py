# news/views.py
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView

from .models import (
    Village, Mahalla, ElectricSupply, WaterSupply,
    Education, Healthcare, PoliceNotice, News, Contact,
    Department, GasSupply
)

from .serializers import (
    VillageSerializer, MahallaSerializer, ElectricSupplySerializer,
    WaterSupplySerializer, EducationSerializer, HealthcareSerializer,
    PoliceNoticeSerializer, NewsSerializer, ContactSerializer,
    DepartmentSerializer, GasSupplySerializer
)

# 📍 Mahalla View
class MahallaViewSet(viewsets.ModelViewSet):
    queryset = Mahalla.objects.all()
    serializer_class = MahallaSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['get'])
    def villages(self, request, pk=None):
        mahalla = self.get_object()
        villages = Village.objects.filter(mahallalar=mahalla)
        serializer = VillageSerializer(villages, many=True)
        return Response(serializer.data)

# 📍 Village View
class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [AllowAny]

# 📍 Electric Supply View
class ElectricSupplyViewSet(viewsets.ModelViewSet):
    queryset = ElectricSupply.objects.all().order_by('-created_at')
    serializer_class = ElectricSupplySerializer
    permission_classes = [AllowAny]

# 📍 Police Notice View
class PoliceNoticeViewSet(viewsets.ModelViewSet):
    queryset = PoliceNotice.objects.all().order_by('-created_at')
    serializer_class = PoliceNoticeSerializer
    permission_classes = [AllowAny]

# 📍 Water Supply View
class WaterSupplyViewSet(viewsets.ModelViewSet):
    queryset = WaterSupply.objects.all().order_by('-created_at')
    serializer_class = WaterSupplySerializer
    permission_classes = [AllowAny]

# 📍 Gas Supply List View
class GasSupplyListCreateView(generics.ListCreateAPIView):
    queryset = GasSupply.objects.all().order_by('-created_at')
    serializer_class = GasSupplySerializer
    permission_classes = [AllowAny]

# 📍 Gas Supply Detail View (Retrieve, Update, Delete)
class GasSupplyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GasSupply.objects.all()
    serializer_class = GasSupplySerializer
    permission_classes = [AllowAny]

# 📍 Education View
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().order_by('-created_at')
    serializer_class = EducationSerializer
    permission_classes = [AllowAny]

# 📍 Healthcare View
class HealthcareViewSet(viewsets.ModelViewSet):
    queryset = Healthcare.objects.all().order_by('-created_at')
    serializer_class = HealthcareSerializer
    permission_classes = [AllowAny]

# 📍 News View
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'], url_path='departments/(?P<department_slug>[^/.]+)')
    def by_department(self, request, department_slug=None):
        queryset = self.queryset.filter(department=department_slug)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# 📍 Contact View
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

# 📍 Faqat o‘qish uchun News (Frontend)
class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # Autentifikatsiyani o'chirish

# 📍 Department View
class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

# 📍 News Detail View (Yangilikni ID bo'yicha olish)
class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'