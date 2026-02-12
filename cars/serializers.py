from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Car
        fields = ['id', 'title', 'brand', 'model_name', 'year', 'price',
                  'transmission', 'mileage', 'image', 'description',
                  'owner_name', 'created_at']