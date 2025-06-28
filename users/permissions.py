from rest_framework import permissions

class IsDepartmentWorker(permissions.BasePermission):
    """
    Faqatgina foydalanuvchi o'z departmentiga tegishli bo'lsa, kirishga ruxsat beriladi.
    """

    def has_permission(self, request, view):
        user = request.user
        # Agar foydalanuvchi admin bo'lsa, hamma joyga kira oladi
        if user.is_authenticated and user.role == 'admin':
            return True
        
        # Agar foydalanuvchi oddiy foydalanuvchi bo'lsa, faqat o'qish huquqi bor
        if user.is_authenticated and user.role == 'user':
            return request.method in permissions.SAFE_METHODS

        # Agar foydalanuvchi xodim bo'lsa, faqat o'z bo'limidagi ma'lumotlarga kirish huquqi
        if user.is_authenticated and user.role == 'worker':
            # view ichida department nomi mavjud bo'lishi kerak (keyin ko'ramiz)
            department = getattr(view, 'department', None)
            return department is not None and user.department == department

        return False
