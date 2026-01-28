from celery import shared_task

@shared_task
def send_appointment_reminder(appointment_id):
    print(f"Reminder sent for appointment {appointment_id}")
