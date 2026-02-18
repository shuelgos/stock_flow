from rest_framework import serializers
from .models import Product,StockMovement

class ProductSerializer(serializers.ModelSerializer):
    current_stock = serializers.IntegerField(read_only=True)
    
    class Meta:
        model =Product
        fields=['id','product','quantity','']
        
class StockMovementSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = StockMovement
        fields=['id','product','quantity','movement_type','created_at']
                
        
        