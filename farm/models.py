from django.db import models
from django.conf import settings 
from authentication.models import TrackObjectStateMixin
# Create your models here.


class FarmData(TrackObjectStateMixin):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('name', 'owner')

    def __str__(self):
        return self.name

class CropData(TrackObjectStateMixin):
    name = models.CharField(max_length=255)
    variety = models.CharField(max_length=255)
    planting_date = models.DurationField(null=True)
    harvest_date = models.DurationField(null=True)
    farm = models.ForeignKey(FarmData, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.name} - {self.variety}"

class SensorData(TrackObjectStateMixin):
    timestamp = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    crop = models.ForeignKey(CropData, on_delete=models.CASCADE)

    def __str__(self):
        return f"SensorData at {self.timestamp} for {self.crop}"