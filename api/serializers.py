from rest_framework import serializers
from .models import *

class enodeb_serializer(serializers.ModelSerializer):
    class Meta:
        model = enodeb
        fields = '__all__'