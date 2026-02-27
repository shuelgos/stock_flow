from rest_framework import viewsets
from .models import Product, StockMovement
from .serializers import ProductSerializer, StockMovementSerializer
from .pagination import StandardResultsSetPagination
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields=['name','is_active','minimum_stock']
    search_fields=['name','description']
    ordering_fields=['name','minimum_stock','created_at']
    ordering=['-created_at']
    permission_classes= [IsAdminOrReadOnly]
    
    @action(detail=False,methods=['get'])
    def low_stock(self,request):
        products=self.get_queryset()
        
        low_stock_products=[
            p for p in products
            if p.current_stock < p.minimum_stock
        ]
        
        serializer=self.get_serializer(low_stock_products,many=True)
        return Response (serializer.data)
        
    @action (detail=False,methods=['get'])
    def summary(self,request):
        products=self.get_queryset() 
        
        low_stock_products = [
        p for p in products
        if p.current_stock < p.minimum_stock
        ]
        total_products= products.count()
        active_products= products.filter(is_active=True).count()
        low_stock_count=len(low_stock_products)
        total_stock_units = sum(p.current_stock for p in products)
        
        data = {
            "total_products": total_products,
            "active_products": active_products,
            "low_stock_products": low_stock_count,
            "total_stock_units": total_stock_units,
        }
        
        return Response(data)
    
    @action (detail=True,methods=['get'])
    def movements(self,request,pk=None):
        
        product= self.get_object()
        movements=product.movements.all()
        serializer= StockMovementSerializer(
            movements,
            many=True,
            context={
                'request':request
            }
        )
        
                
        
        
        
        
        
    
              
    
class StockMovementViewSet (viewsets.ModelViewSet):
    queryset=StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    pagination_class = StandardResultsSetPagination    
    
    
    
    