from rest_framework.viewsets import ModelViewSet
from .models import Prescription
from .serializers import PrescriptionSerializer
from rest_framework.permissions import IsAuthenticated

class PrescriptionViewSet(ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
