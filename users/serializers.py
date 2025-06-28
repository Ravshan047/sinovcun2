# from rest_framework import serializers
# from .models import CustomUser, Profile
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# # 1. JWT login serializer
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['username'] = user.username
#         token['phone_number'] = user.phone_number
#         return token

# # 2. Register serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password', 'email', 'phone_number']

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data.get('email'),
#             password=validated_data['password'],
#             phone_number=validated_data.get('phone_number')
#         )
#         # Profile modelini avtomatik yaratamiz
#         Profile.objects.create(user=user)
#         return user

# # 3. Foydalanuvchi uchun qisqacha ma'lumot
# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'phone_number']
#         read_only_fields = fields

# # 4. Profile modelining to‘liq serializeri
# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserProfileSerializer(read_only=True)
#     bio = serializers.CharField(required=False, allow_blank=True, allow_null=True)
#     avatar = serializers.ImageField(required=False, allow_null=True)

#     class Meta:
#         model = Profile
#         fields = ['user', 'bio', 'avatar']

#     def update(self, instance, validated_data):
#         instance.bio = validated_data.get('bio', instance.bio)
#         instance.avatar = validated_data.get('avatar', instance.avatar)
#         instance.save()
#         return instance

#     def create(self, validated_data):
#         # Bu holatda user tashqaridan berilmaydi — avtomatik bog‘lanadi
#         user = self.context['request'].user
#         return Profile.objects.create(user=user, **validated_data)






# from rest_framework import serializers
# from .models import CustomUser, Profile
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# # 1. JWT login serializer (foydalanuvchidan token olganda qo‘shimcha ma’lumotlar qaytariladi)
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['username'] = user.username
#         token['phone_number'] = user.phone_number
#         token['role'] = user.role
#         token['department'] = user.department
#         return token

# # 2. Ro‘yxatdan o‘tish uchun serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)
#     role = serializers.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=False)
#     department = serializers.ChoiceField(choices=CustomUser.DEPARTMENT_CHOICES, required=False)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password', 'email', 'phone_number', 'role', 'department']

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data.get('email'),
#             password=validated_data['password'],
#             phone_number=validated_data.get('phone_number'),
#             role=validated_data.get('role', 'user'),
#             department=validated_data.get('department')
#         )
#         Profile.objects.create(user=user)
#         return user

# # 3. Foydalanuvchi uchun umumiy ma’lumotlar
# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'phone_number', 'role', 'department']
#         read_only_fields = fields

# # 4. Profile modelining to‘liq serializeri
# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserProfileSerializer(read_only=True)
#     bio = serializers.CharField(required=False, allow_blank=True, allow_null=True)
#     avatar = serializers.ImageField(required=False, allow_null=True)

#     class Meta:
#         model = Profile
#         fields = ['user', 'bio', 'avatar']

#     def update(self, instance, validated_data):
#         instance.bio = validated_data.get('bio', instance.bio)
#         instance.avatar = validated_data.get('avatar', instance.avatar)
#         instance.save()
#         return instance

#     def create(self, validated_data):
#         user = self.context['request'].user
#         return Profile.objects.create(user=user, **validated_data)







# from rest_framework import serializers
# from .models import CustomUser, Profile, Department  # Department modelini import qildik
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# # 1. JWT login serializer
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['username'] = user.username
#         token['phone_number'] = user.phone_number
#         token['role'] = user.role
#         token['department'] = user.department.id if user.department else None
#         return token

# # 2. Ro‘yxatdan o‘tish uchun serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)
#     role = serializers.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=False)
#     department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), required=False)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password', 'email', 'phone_number', 'role', 'department']

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data.get('email'),
#             password=validated_data['password'],
#             phone_number=validated_data.get('phone_number'),
#             role=validated_data.get('role', 'user'),
#             department=validated_data.get('department')
#         )
#         Profile.objects.create(user=user)
#         return user

# # 3. Foydalanuvchi uchun umumiy ma’lumotlar
# class UserProfileSerializer(serializers.ModelSerializer):
#     department = serializers.StringRelatedField()

#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'phone_number', 'role', 'department']
#         read_only_fields = fields

# # 4. Profile modelining to‘liq serializeri
# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserProfileSerializer(read_only=True)
#     bio = serializers.CharField(required=False, allow_blank=True, allow_null=True)
#     avatar = serializers.ImageField(required=False, allow_null=True)

#     class Meta:
#         model = Profile
#         fields = ['user', 'bio', 'avatar']

#     def update(self, instance, validated_data):
#         instance.bio = validated_data.get('bio', instance.bio)
#         instance.avatar = validated_data.get('avatar', instance.avatar)
#         instance.save()
#         return instance

#     def create(self, validated_data):
#         user = self.context['request'].user
#         return Profile.objects.create(user=user, **validated_data)



















# from rest_framework import serializers
# from .models import CustomUser, Profile, Department
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# # ✅ 1. JWT token serializer — login uchun
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['username'] = user.username
#         token['phone_number'] = user.phone_number
#         token['role'] = user.role
#         token['department'] = user.department.name if user.department else None
#         return token


# # ✅ 2. Register (ro‘yxatdan o‘tish) serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     role = serializers.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=False)
#     department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), required=False)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password', 'email', 'phone_number', 'role', 'department']

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data.get('email'),
#             password=validated_data['password'],
#             phone_number=validated_data.get('phone_number'),
#             role=validated_data.get('role', 'user'),
#             department=validated_data.get('department')
#         )
#         # Avtomatik tarzda profile yaratiladi
#         Profile.objects.create(user=user)
#         return user


# # ✅ 3. CustomUser (faqat o‘qish uchun) serializer — profil ichida ishlatiladi
# class UserProfileSerializer(serializers.ModelSerializer):
#     department = serializers.StringRelatedField()

#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'phone_number', 'role', 'department']
#         read_only_fields = fields


# # ✅ 4. Profile serializer — avatar, bio, va foydalanuvchi
# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserProfileSerializer(read_only=True)
#     bio = serializers.CharField(required=False, allow_blank=True, allow_null=True)
#     avatar = serializers.ImageField(required=False, allow_null=True)

#     class Meta:
#         model = Profile
#         fields = ['user', 'bio', 'avatar']

#     def update(self, instance, validated_data):
#         instance.bio = validated_data.get('bio', instance.bio)
#         avatar = validated_data.get('avatar')
#         if avatar is not None:
#             instance.avatar = avatar
#         instance.save()
#         return instance

#     def create(self, validated_data):
#         user = self.context['request'].user
#         return Profile.objects.create(user=user, **validated_data)


from rest_framework import serializers
from .models import CustomUser, Profile, Department
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# ✅ 1. JWT token serializer — login uchun
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['phone_number'] = user.phone_number
        token['role'] = user.role
        token['department'] = user.department.name if user.department else None
        return token


# ✅ 2. Register (ro‘yxatdan o‘tish) serializer — faqat oddiy foydalanuvchi
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'phone_number']

    def create(self, validated_data):
        # Faqat oddiy foydalanuvchi bo‘lib yaratiladi
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number'),
            role='user',  # Har doim oddiy user
            department=None  # Hali bo‘lim tanlanmaydi
        )
        # Profile avtomatik yaratiladi
        Profile.objects.create(user=user)
        return user


# ✅ 3. CustomUser (faqat o‘qish uchun) serializer — profil ichida ishlatiladi
class UserProfileSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'role', 'department']
        read_only_fields = fields


# ✅ 4. Profile serializer — avatar, bio, va foydalanuvchi
class ProfileSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    bio = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    avatar = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'avatar']

    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        avatar = validated_data.get('avatar')
        if avatar is not None:
            instance.avatar = avatar
        instance.save()
        return instance

    def create(self, validated_data):
        user = self.context['request'].user
        return Profile.objects.create(user=user, **validated_data)
