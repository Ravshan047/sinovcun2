from rest_framework import serializers
from .models import (
    Village, Mahalla, ElectricSupply, WaterSupply,
    Education, Healthcare, PoliceNotice, News, Contact,
    Department, GasSupply  # ← GasSupply shu yerga qo‘shilgan
)

# 📍 Mahalla serializer
class MahallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahalla
        fields = ['id', 'name']

class MahallaForSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahalla
        fields = ['id', 'name']

class VillageForSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = ['id', 'name']

# 📍 Village serializer
class VillageSerializer(serializers.ModelSerializer):
    mahallalar = MahallaSerializer(many=True, read_only=True)


    class Meta:
        model = Village
        fields = ['id', 'name', 'mahallalar']

# 📍 Elektr ta'minoti
class ElectricSupplySerializer(serializers.ModelSerializer):
    mahalla = MahallaForSerializer(many=True, read_only=True)
    village = VillageForSerializer(many=True, read_only=True)
    class Meta:
        model = ElectricSupply
        fields = '__all__'

# 📍 Politsiya
class PoliceNoticeSerializer(serializers.ModelSerializer):
    mahalla = MahallaForSerializer(many=True, read_only=True)
    village = VillageForSerializer(many=True, read_only=True)
    class Meta:
        model = PoliceNotice
        fields = '__all__'


# 📍 Suv ta'minoti
class WaterSupplySerializer(serializers.ModelSerializer):
    mahalla = MahallaForSerializer(many=True, read_only=True)
    village = VillageForSerializer(many=True, read_only=True)
    class Meta:
        model = WaterSupply
        fields = '__all__'


# 📍 Gaz ta'minoti 
class GasSupplySerializer(serializers.ModelSerializer):
    mahalla = MahallaForSerializer(many=True, read_only=True)
    village = VillageForSerializer(many=True, read_only=True)
    class Meta:
        model = GasSupply
        fields = '__all__'

# class GasSupplySerializer(serializers.ModelSerializer):
#     mahalla = MahallaForSerializer(many=True, read_only=True)
#     village = VillageForSerializer(many=True, read_only=True)
#     class Meta:
#         model = GasSupply
#         fields = '__all__'



# 📍 Ta'lim
class EducationSerializer(serializers.ModelSerializer):
    mahalla = MahallaForSerializer(many=True, read_only=True)
    village = VillageForSerializer(many=True, read_only=True)
    class Meta:
        model = Education
        fields = '__all__'

# 📍 Sog‘liqni saqlash
class HealthcareSerializer(serializers.ModelSerializer):
    mahalla = MahallaForSerializer(many=True, read_only=True)
    village = VillageForSerializer(many=True, read_only=True)
    class Meta:
        model = Healthcare
        fields = '__all__'


# 📍 Yangiliklar
class NewsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)

    class Meta:
        model = News
        fields = [
            'id',
            'titleUz', 'titleRu',
            'contentUz', 'contentRu',
            'image', 'video',
            'department',
            'date'
        ]

# 📍 Kontakt
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

# 📍 Bo‘limlar (departments)
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


