from celery import shared_task
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

@shared_task
def generate_prescription_pdf(prescription_id):

    file_name = f"/app/prescription_{prescription_id}.pdf"

    c = canvas.Canvas(file_name, pagesize=A4)
    c.drawString(100, 750, f"Prescription ID: {prescription_id}")
    c.save()

    print("PDF generated:", file_name)
