from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet

router = DefaultRouter()
router.register("", InvoiceViewSet)

urlpatterns = router.urls
