from django.db import models
from apps.patients.models import Patient

class MedicalDocument(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to="medical_docs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file)
