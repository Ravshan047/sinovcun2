# from django.urls import path
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# from .views import (
#     MyTokenObtainPairView,
#     RegisterView,
#     ProfileView,
#     LogoutView,
#     ElectricSupplyStaffView,
#     DepartmentLoginView,
# )

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Users API",
#         default_version='v1',
#         description="Foydalanuvchi va xodimlar uchun API",
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

# urlpatterns = [
#     path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('profile/', ProfileView.as_view(), name='profile'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('electric-supply/', ElectricSupplyStaffView.as_view(), name='electric_supply'),
#     path('department-login/', DepartmentLoginView.as_view(), name='department_login'),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
# ]






from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    MyTokenObtainPairView,
    RegisterView,
    ProfileView,
    LogoutView,
    ElectricSupplyStaffView,
    # DepartmentLoginView,  # Bu qatordan # olib tashlang (o‘chiring)
)

schema_view = get_schema_view(
    openapi.Info(
        title="Users API",
        default_version='v1',
        description="Foydalanuvchi va xodimlar uchun API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('electric-supply/', ElectricSupplyStaffView.as_view(), name='electric_supply'),
    # path('department-login/', DepartmentLoginView.as_view(), name='department_login'),  # Bu qatordan # olib tashlang (o‘chiring)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
