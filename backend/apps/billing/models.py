from django.db import models
from apps.patients.models import Patient

class Invoice(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.amount}"
