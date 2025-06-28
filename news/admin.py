from django.contrib import admin
from django import forms
from .models import (
    Village, Mahalla, ElectricSupply, WaterSupply,
    Education, Healthcare, PoliceNotice, News, Contact
)

#   Elektr ta'minoti uchun forma (clean() metodi ishlashi uchun)
class ElectricSupplyForm(forms.ModelForm):
    class Meta:
        model = ElectricSupply
        fields = '__all__'

    # def clean(self):
    #     cleaned_data = super().clean()
    #     village = cleaned_data.get('village')
    #     mahalla = cleaned_data.get('mahalla')
    #     if village and mahalla and not mahalla.villages.filter(id=village.id).exists():
    #         raise forms.ValidationError("Tanlangan mahalla ushbu qishloqqa tegishli emas.")
    #     return cleaned_data

#  Elektr admin
@admin.register(ElectricSupply)
class ElectricSupplyAdmin(admin.ModelAdmin):
    form = ElectricSupplyForm
    list_display = ['reason', 'start_time', 'end_time']
    list_filter = ['village', 'mahalla']

#  Mahalla admini
@admin.register(Mahalla)
class MahallaAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['villages']

#  Qishloq admini
@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ['name']

#  Oddiy adminlar (hozircha validatsiya yo‘q)
admin.site.register(WaterSupply)
admin.site.register(Education)
admin.site.register(Healthcare)
admin.site.register(PoliceNotice)
admin.site.register(News)
admin.site.register(Contact)

from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameUz', 'contactPhone')  # ✅ to‘g‘ri nom


from .models import GasSupply
@admin.register(GasSupply)
class GasSupplyAdmin(admin.ModelAdmin):
    list_display = ('reason', 'start_time', 'end_time')
    filter_horizontal = ('village', 'mahalla')  # ManyToMany maydonlar uchun qulay tanlash