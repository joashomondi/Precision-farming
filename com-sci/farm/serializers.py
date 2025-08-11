from rest_framework import serializers 
from .models import FarmData, CropData, SensorData 


class FarmDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FarmData 
        exclude = ('owner', 'date_created')
        
        
class CropDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CropData 
        exclude = ('harvest_date', 'planting_date', 'date_created')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('name', 'farm'),
                message="A crop with this name has already been associated with this farm"
            )
        ]
