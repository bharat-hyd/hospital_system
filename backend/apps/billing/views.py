from rest_framework.viewsets import ModelViewSet
from .models import Invoice
from .serializers import InvoiceSerializer
from rest_framework.permissions import IsAuthenticated
from .tasks import generate_invoice_pdf

class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        invoice = serializer.save()
        generate_invoice_pdf.delay(invoice.id)
