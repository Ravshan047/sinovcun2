# # from django.contrib import admin
# # from .models import CustomUser, Profile
# # from django.contrib.auth.admin import UserAdmin

# # @admin.register(CustomUser)
# # class CustomUserAdmin(UserAdmin):
# #     model = CustomUser
# #     list_display = ('username', 'email', 'phone_number', 'is_staff')
# #     fieldsets = UserAdmin.fieldsets + (
# #         (None, {'fields': ('phone_number',)}),  # <-- Vergul kerak
# #     )

# # @admin.register(Profile)
# # class ProfileAdmin(admin.ModelAdmin):
# #     list_display = ('user', )
# #     search_fields = ('user__username',)



# from django.contrib import admin
# from .models import CustomUser, Profile
# from django.contrib.auth.admin import UserAdmin

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'phone_number', 'role', 'department', 'is_staff')
    
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {
#             'fields': ('phone_number', 'role', 'department')
#         }),
#     )
    
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {
#             'fields': ('phone_number', 'role', 'department'),
#         }),
#     )

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', )
#     search_fields = ('user__username',)





# from django.contrib import admin
# from .models import CustomUser, Profile
# from django.contrib.auth.admin import UserAdmin

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'phone_number', 'role', 'department', 'is_staff', 'is_superuser')
#     list_filter = ('role', 'department', 'is_staff', 'is_superuser')
#     search_fields = ('username', 'email', 'phone_number')

#     fieldsets = UserAdmin.fieldsets + (
#         (None, {
#             'fields': ('phone_number', 'role', 'department')
#         }),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {
#             'fields': ('phone_number', 'role', 'department'),
#         }),
#     )

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', )
#     search_fields = ('user__username',)




# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser, Profile, Department

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'phone_number', 'role', 'department', 'is_staff')
#     list_filter = ('role', 'department')
#     search_fields = ('username', 'email', 'department__name')

#     fieldsets = UserAdmin.fieldsets + (
#         (None, {
#             'fields': ('phone_number', 'role', 'department')
#         }),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {
#             'fields': ('phone_number', 'role', 'department'),
#         }),
#     )

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', )
#     search_fields = ('user__username',)

# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)







# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.utils.html import format_html
# from .models import CustomUser, Profile, Department
# from .forms import DepartmentAdminForm  # formni chaqirib olayapmiz

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'phone_number', 'role', 'department', 'is_staff')
#     list_filter = ('role', 'department')
#     search_fields = ('username', 'email', 'department__name')

#     fieldsets = UserAdmin.fieldsets + (
#         (None, {
#             'fields': ('phone_number', 'role', 'department')
#         }),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {
#             'fields': ('phone_number', 'role', 'department'),
#         }),
#     )


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user',)
#     search_fields = ('user__username',)


# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     form = DepartmentAdminForm  # maxsus forma
#     list_display = ('name', 'login', 'password_display')
#     search_fields = ('name', 'login')
#     fields = ('name', 'login', 'password')

#     def password_display(self, obj):
#         return format_html('<span style="color: gray;">********</span>')

#     password_display.short_description = 'Password'




# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.utils.html import format_html
# from .models import CustomUser, Profile, Department
# from .forms import DepartmentAdminForm  # formni chaqirib olayapmiz

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'phone_number', 'role', 'department', 'is_staff')
#     list_filter = ('role', 'department')
#     search_fields = ('username', 'email', 'department__name')

#     fieldsets = UserAdmin.fieldsets + (
#         (None, {
#             'fields': ('phone_number', 'role', 'department')
#         }),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'role', 'department'),
#         }),
#     )


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user',)
#     search_fields = ('user__username',)


# # @admin.register(Department)
# # class DepartmentAdmin(admin.ModelAdmin):
# #     form = DepartmentAdminForm  # maxsus forma
# #     # list_display = ('name', 'login', 'password_display')
# #     search_fields = ('name', 'login')
# #     # fields = ('name', 'login', 'password')

# #     def password_display(self, obj):
# #         return format_html('<span style="color: gray;">********</span>')

# #     password_display.short_description = 'Password'



# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     form = DepartmentAdminForm
#     list_display = ('name', 'login', 'password_display')
#     search_fields = ('name', 'login')
#     fields = ('name', 'login', 'password')

#     def password_display(self, obj):
#         return format_html('<span style="color: gray;">********</span>')

#     password_display.short_description = 'Password'

#     def has_change_permission(self, request, obj=None):
#         return request.user.is_superuser



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser, Profile, Department
from .forms import DepartmentAdminForm


# ✅ CustomUser ni admin panelda ko‘rsatish
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone_number', 'role', 'department', 'is_staff')
    list_filter = ('role', 'department')
    search_fields = ('username', 'email', 'department__name')

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('phone_number', 'role', 'department'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'role', 'department'),
        }),
    )


# ✅ Profile modeli uchun admin sozlamasi
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)


# ✅ Department modeli uchun admin forma, maxfiy parol ko‘rinishi va superuserga ruxsat
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentAdminForm
    list_display = ('name', 'login', 'password_display')
    search_fields = ('name', 'login')
    fields = ('name', 'login', 'password')

    def password_display(self, obj):
        return format_html('<span style="color: gray;">********</span>')

    password_display.short_description = 'Password'

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # Faqat superuser o‘zgartira oladi
