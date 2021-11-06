from django.db import models
from rest_framework import fields, serializers
from .models import Ish

class IshSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ish
        fields = '__all__'