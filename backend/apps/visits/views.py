from rest_framework.viewsets import ModelViewSet
from .models import Visit
from .serializers import VisitSerializer
from rest_framework.permissions import IsAuthenticated

class VisitViewSet(ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]
