# from rest_framework.views import APIView
# from rest_framework import generics, permissions, status
# from rest_framework.permissions import IsAuthenticated, BasePermission
# from rest_framework.response import Response
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.tokens import RefreshToken

# from .models import CustomUser, Profile
# from .serializers import (
#     MyTokenObtainPairSerializer,
#     RegisterSerializer,
#     ProfileSerializer
# )


# class MyTokenObtainPairView(TokenObtainPairView):
#     """JWT orqali login qilish"""
#     serializer_class = MyTokenObtainPairSerializer


# class RegisterView(generics.CreateAPIView):
#     """Foydalanuvchini ro'yxatdan o'tkazish"""
#     queryset = CustomUser.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = [permissions.AllowAny]


# class ProfileView(generics.RetrieveUpdateAPIView):
#     """Foydalanuvchi profilini ko‘rish va tahrirlash"""
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         profile, created = Profile.objects.get_or_create(user=self.request.user)
#         return profile


# class LogoutView(APIView):
#     """Foydalanuvchini tizimdan chiqarish (logout)"""
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         try:
#             refresh_token = request.data.get("refresh")
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response({"detail": "Logged out successfully."}, status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# class ElectricSupplyStaffView(APIView):
#     """Elektr xodimlari uchun API"""
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"message": "Electric staff info"})


# class DepartmentLoginView(APIView):
#     """Bo‘lim login qilish uchun API"""
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         return Response({"message": "Login logic here"})


from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser, Profile, Department
from .serializers import (
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    ProfileSerializer
)


class MyTokenObtainPairView(TokenObtainPairView):
    """JWT orqali login qilish"""
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    """Foydalanuvchini ro'yxatdan o'tkazish"""
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.RetrieveUpdateAPIView):
    """Foydalanuvchi profilini ko‘rish va tahrirlash"""
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


class LogoutView(APIView):
    """Foydalanuvchini tizimdan chiqarish (logout)"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logged out successfully."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ElectricSupplyStaffView(APIView):
    """Elektr xodimlari uchun API"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Electric staff info"})


class BecomeStaffView(APIView):
    """Xodim bo‘lib ro‘yxatdan o‘tish uchun login va parol"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        dept_id = request.data.get("department_id")
        staff_login = request.data.get("login")
        staff_password = request.data.get("password")

        if not all([dept_id, staff_login, staff_password]):
            return Response({"error": "Barcha maydonlar to‘ldirilishi shart."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            department = Department.objects.get(id=dept_id)
        except Department.DoesNotExist:
            return Response({"error": "Bo‘lim topilmadi."}, status=status.HTTP_404_NOT_FOUND)

        # Agar bo'limga allaqachon biriktirilgan xodim bo'lsa
        if department.staff_user is not None:
            return Response({"error": "Bu bo‘limga allaqachon xodim biriktirilgan."}, status=status.HTTP_400_BAD_REQUEST)

        # Login va parol tekshiruvi
        if department.staff_login != staff_login or department.staff_password != staff_password:
            return Response({"error": "Login yoki parol noto‘g‘ri."}, status=status.HTTP_401_UNAUTHORIZED)

        # Foydalanuvchini xodim sifatida yangilash
        user.role = 'staff'
        user.department = department
        user.save()

        # Bo‘limga xodim biriktirish
        department.staff_user = user
        department.save()

        return Response({"detail": f"{department.name} bo‘limiga xodim sifatida qo‘shildingiz."})
