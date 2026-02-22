from rest_framework.viewsets import ModelViewSet
from .models import Payment
from .serializer import PaymentSerializer

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer