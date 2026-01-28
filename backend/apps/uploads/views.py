from rest_framework.viewsets import ModelViewSet
from .models import MedicalDocument
from .serializers import MedicalDocumentSerializer
from rest_framework.permissions import IsAuthenticated

class MedicalDocumentViewSet(ModelViewSet):
    queryset = MedicalDocument.objects.all()
    serializer_class = MedicalDocumentSerializer
    permission_classes = [IsAuthenticated]
