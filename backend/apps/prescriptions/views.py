from rest_framework.viewsets import ModelViewSet
from .models import Prescription
from .serializers import PrescriptionSerializer
from rest_framework.permissions import IsAuthenticated
from .tasks import generate_prescription_pdf

class PrescriptionViewSet(ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        prescription = serializer.save()
        generate_prescription_pdf.delay(prescription.id)
