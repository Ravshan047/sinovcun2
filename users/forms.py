# from django import forms
# from .models import Department

# class DepartmentAdminForm(forms.ModelForm):
#     password = forms.CharField(required=False, widget=forms.PasswordInput)

#     class Meta:
#         model = Department
#         fields = ['name', 'login', 'password']

#     def save(self, commit=True):
#         department = super().save(commit=False)
#         password = self.cleaned_data.get('password')
#         if password:
#             department.set_password(password)
#         if commit:
#             department.save()
#         return department






from django import forms
from .models import Department

# class DepartmentAdminForm(forms.ModelForm):
#     password = forms.CharField(required=False, widget=forms.PasswordInput)

#     class Meta:
#         model = Department
#         fields = ['name', 'login', 'password']

#     def save(self, commit=True):
#         department = super().save(commit=False)
#         password = self.cleaned_data.get('password')
#         if password:
#             department.password = password  
#         if commit:
#             department.save()
#         return department



class DepartmentAdminForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = Department
        fields = ['name', 'login', 'password']

    def save(self, commit=True):
        department = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            department.password = password  # oddiy saqlash
        if commit:
            department.save()
        return department
