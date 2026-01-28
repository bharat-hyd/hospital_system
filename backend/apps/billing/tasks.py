from celery import shared_task
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

@shared_task
def generate_invoice_pdf(invoice_id):

    file_name = f"/app/invoice_{invoice_id}.pdf"

    c = canvas.Canvas(file_name, pagesize=A4)
    c.drawString(100, 750, f"Invoice ID: {invoice_id}")
    c.save()

    print("Invoice PDF generated:", file_name)
