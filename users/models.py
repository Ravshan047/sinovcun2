# # 1. models.py
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.conf import settings

# class CustomUser(AbstractUser):
#     phone_number = models.CharField(max_length=20, null=True, blank=True)

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
#     bio = models.TextField(null=True, blank=True)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

#     def __str__(self):
#         return f"{self.user.username} profile"






# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser, Profile, Department
# from django.utils.translation import gettext_lazy as _


# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'phone_number', 'role', 'department', 'is_staff')
#     list_filter = ('role', 'department')
#     search_fields = ('username', 'email', 'department__name')

#     fieldsets = UserAdmin.fieldsets + (
#         (_('Qo‘shimcha ma’lumotlar'), {
#             'fields': ('phone_number', 'role', 'department'),
#         }),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (_('Qo‘shimcha ma’lumotlar'), {
#             'fields': ('phone_number', 'role', 'department'),
#         }),
#     )

#     # Admin menyuda nomini o‘zgartiramiz
#     def get_model_perms(self, request):
#         """
#         Bu modelni admin menyuda 'Employees' nomi bilan chiqarish uchun.
#         """
#         perms = super().get_model_perms(request)
#         if perms:
#             perms['view'] = True
#         return perms

#     def changelist_view(self, request, extra_context=None):
#         extra_context = extra_context or {}
#         extra_context['title'] = 'Employees'
#         return super().changelist_view(request, extra_context=extra_context)

#     def get_queryset(self, request):
#         return super().get_queryset(request).select_related('department')


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user',)
#     search_fields = ('user__username',)


# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'login')
#     search_fields = ('name', 'login')
#     fields = ('name', 'login')

#     def save_model(self, request, obj, form, change):
#         if 'password_hash' in form.cleaned_data:
#             obj.set_password(form.cleaned_data['password_hash'])
#         super().save_model(request, obj, form, change)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Department(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
      
    )

    email = models.EmailField(unique=True, blank=False, null=False)  # <== Emailni unikal qilib belgiladik
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, null=True, blank=True)  # lavozim yoki rol
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"
