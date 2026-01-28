from django.db import models
from apps.appointments.models import Appointment

class Visit(models.Model):

    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    notes = models.TextField()
    diagnosis = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.appointment)
