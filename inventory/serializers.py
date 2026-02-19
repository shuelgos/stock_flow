from rest_framework import serializers
from .models import Product,StockMovement

class ProductSerializer(serializers.ModelSerializer):
    current_stock = serializers.IntegerField(read_only=True)
    
    class Meta:
        model =Product
        fields=['id','name','description','minimum_stock','is_active','created_at','current_stock']
        
class StockMovementSerializer (serializers.ModelSerializer):
    
    def validate(self,attrs):
        product= attrs.get('product')
        quantity=attrs.get('quantity')
        movement_type=attrs.get('movement_type')
        
        if product.is_active == False:
            raise serializers.ValidationError("No se pueden registrar movimientos para productos inactivos")
                
        if movement_type=='OUT':
            current_stock= product.current_stock
            if quantity > current_stock:
                raise serializers.ValidationError("La cantidad no puede ser mayor al stock")
            
        return attrs    
    
    class Meta:
        model = StockMovement
        fields=['id','product','quantity','movement_type','created_at']
        
        
                
        
        