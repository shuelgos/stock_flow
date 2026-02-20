from rest_framework import viewsets
from .models import Product, StockMovement
from .serializers import ProductSerializer, StockMovementSerializer
from .pagination import StandardResultsSetPagination

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields=['name','is_active','minimum_stock']
    search_fields=['name','description']
    ordering_fields=['name','minimum_stock','created_at']
    ordering=['-created_at']
    
class StockMovementViewSet (viewsets.ModelViewSet):
    queryset=StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    pagination_class = StandardResultsSetPagination    
    
    
    
    