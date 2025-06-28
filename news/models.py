# from django.db import models



# class Mahalla(models.Model):
#     name = models.CharField(max_length=100)

#     class Meta:
#         unique_together = ('name')

#     def __str__(self):
#         return f"{self.name} (Qishloq: {self.village.name})"


# class Village(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     village = models.ForeignKey(Mahalla, on_delete=models.CASCADE, related_name='mahallalar')

#     def __str__(self):
#         return self.name


# class ElectricSupply(models.Model):
#     mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, null=True, blank=True)
#     village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True)
#     reason = models.TextField()
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Tok o‘chishi - {self.location.name}"

# class WaterSupply(models.Model):
#     mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, null=True, blank=True)
#     village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True)
#     reason = models.TextField()
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Suv o‘chishi - {self.location.name}"

# class Education(models.Model):
#     mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, null=True, blank=True)
#     village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True)
#     message = models.TextField()
#     date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Ta’lim - {self.location.name}"

# class Healthcare(models.Model):
#     mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, null=True, blank=True)
#     village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True)
#     message = models.TextField()
#     date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Sog‘liqni saqlash - {self.location.name}"

# class PoliceNotice(models.Model):
#     mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, null=True, blank=True)
#     village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True)
#     message = models.TextField()
#     date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Politsiya - {self.location.name}"

# class News(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     image = models.ImageField(upload_to='news_images/', blank=True, null=True)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()
#     sent_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Xabar - {self.name}"

# from django.db import models
# from django.core.exceptions import ValidationError

# # Qishloq modeli
# class Village(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.name


# # Mahalla modeli
# class Mahalla(models.Model):
#     name = models.CharField(max_length=100)
#     village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='mahallalar')

#     class Meta:
#         unique_together = ('name', 'village')  # Har bir qishloqda bir xil nomli mahalla bo‘lishi mumkin emas

#     def __str__(self):
#         return f"{self.name} ({self.village.name})"

from django.db import models
from django.core.exceptions import ValidationError

# Qishloq modeli
class Village(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Mahalla modeli (ko‘p qishloqni bog‘laydi)
class Mahalla(models.Model):
    name = models.CharField(max_length=100)
    villages = models.ManyToManyField(Village, related_name='mahallalar')

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name

# Elektr ta'minoti
class ElectricSupply(models.Model):
    village = models.ManyToManyField(Village, related_name='electricsupply_village')
    mahalla = models.ManyToManyField(Mahalla, related_name='electricsupply_mahalla')
    reason = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


# Politsiya xabarlari
class PoliceNotice(models.Model):
    village = models.ManyToManyField(Village, related_name='policenotice_village')
    mahalla = models.ManyToManyField(Mahalla, related_name='policenotice_mahalla')
    message = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


# Suv ta'minoti
class WaterSupply(models.Model):
    village = models.ManyToManyField(Village, related_name='watersupply_village')
    mahalla = models.ManyToManyField(Mahalla, related_name='watersupply_mahalla')
    reason = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


#Gaz taminoti
class GasSupply(models.Model):
    village = models.ManyToManyField(Village, related_name='gassupply_village')
    mahalla = models.ManyToManyField(Mahalla, related_name='gassupply_mahalla')
    reason = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gaz uzilishi: {self.reason[:30]}"  


    # def clean(self):
    #     # Har bir mahalla barcha tanlangan qishloqlardan kamida biriga tegishli bo‘lishi kerak
    #     selected_villages = set(self.village.all())
    #     for mahalla in self.mahalla.all():
    #         related_villages = set(mahalla.villages.all())
    #         if not selected_villages & related_villages:
    #             raise ValidationError(f"Mahalla '{mahalla.name}' tanlangan qishloqlardan hech biriga tegishli emas.")

    def __str__(self):
        return f"{self.village.name} - {self.mahalla.name}: Tok o‘chishi"



    def __str__(self):
        return f"{self.village.name} - {self.mahalla.name}: Suv muammosi"
    
  



# Ta'lim yangiliklari
class Education(models.Model):
    village = models.ManyToManyField(Village, related_name='education_village')
    mahalla = models.ManyToManyField(Mahalla, related_name='education_mahalla')
    message = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.village.name} - {self.mahalla.name}: Ta’lim yangilik"

# Sog‘liqni saqlash e'loni
class Healthcare(models.Model):
    village = models.ManyToManyField(Village, related_name='healthcare_village')
    mahalla = models.ManyToManyField(Mahalla, related_name='healthcare_mahalla')
    message = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.village.name} - {self.mahalla.name}: Sog‘liq e’loni"



    def __str__(self):
        return f"{self.village.name} - {self.mahalla.name}: Politsiya xabari"

# Video fayl faqat .mp4 bo‘lishi uchun tekshiruvchi
def validate_mp4(value):
    if not value.name.endswith('.mp4'):
        raise ValidationError("Faqat .mp4 formatdagi videolar qabul qilinadi.")

from django.db import models
from django.core.exceptions import ValidationError

# 📌 Yangilangan DEPARTMENT_CHOICES ni shu yerga yozasiz:
DEPARTMENT_CHOICES = [
    ('electricity', "Elektr"),
    ('gas', "Gaz"),
    ('police', "Politsiya"),
    ('internal-affairs', "Ichki ishlar"),
    ('water', "Suv"),
    ('education', "Ta'lim"),
    ('health', "Sog‘liqni saqlash"),
    ('transport', "Transport"),
    ('other', "Boshqa"),
]

# ✅ News modelida shunday foydalanasiz:
class News(models.Model):
    titleUz = models.CharField(max_length=200)
    titleRu = models.CharField(max_length=200)
    contentUz = models.TextField()
    contentRu = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    video = models.FileField(
        upload_to='news_videos/',
        blank=True,
        null=True,
        validators=[validate_mp4]
    )
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='other')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titleUz


    titleUz = models.CharField(max_length=200)
    titleRu = models.CharField(max_length=200)
    contentUz = models.TextField()
    contentRu = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    video = models.FileField(
        upload_to='news_videos/',
        blank=True,
        null=True,
        validators=[validate_mp4]
    )
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, default='other')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titleUz

# Kontakt (foydalanuvchilardan xabarlar)
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Xabar - {self.name}"

class Department(models.Model):
    # id = models.CharField(max_length=50, primary_key=True)  # slug formatida
    # name = models.CharField(max_length=100)
    # phone = models.CharField(max_length=50)
    # email = models.EmailField()
    # address = models.TextField()
    # working_hours = models.CharField(max_length=100)
    # description = models.TextField(blank=True)
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(unique=True)  # ⚠️ Buni frontend `slug` bilan so‘rov yuboradi
    nameUz = models.CharField(max_length=255)
    descriptionUz = models.TextField()
    contactPhone = models.CharField(max_length=50)
    contactEmail = models.EmailField()
    address = models.CharField(max_length=255)
    workingHours = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)


    def __str__(self):
        return self.nameUz
