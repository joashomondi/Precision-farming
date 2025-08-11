from django.contrib import admin
from .models import FarmData, CropData, SensorData
# Register your models here.


@admin.register(FarmData)
class FarmDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'size', 'owner')
    list_filter = ('location', 'owner')
    
@admin.register(CropData)
class CropDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'variety', 'planting_date', 'farm')
    list_filter = ('farm',)
    
@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'temperature', 'humidity', 'crop')
    list_filter = ('crop',)
