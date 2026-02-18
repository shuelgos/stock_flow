from rest_framework import viewsets
from .models import Product, StockMovement
from .serializers import ProductSerializer, StockMovementSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    
class StockMovementViewSet (viewsets.ModelViewSet):
    query_Set=StockMovement.objetc.all()
    serializer_class = StockMovement    
    