from rest_framework import serializers
from .models import MedicalDocument

class MedicalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalDocument
        fields = "__all__"
