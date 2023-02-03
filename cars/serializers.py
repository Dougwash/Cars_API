from rest_framework import serializes
from .models import Car

class CarSerializer(serializes.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id','make' , 'model' , 'year' , 'price']