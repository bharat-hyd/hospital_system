from django.db import models
from apps.visits.models import Visit

class Prescription(models.Model):

    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, related_name="prescriptions")
    medicine = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)

    def __str__(self):
        return self.medicine
