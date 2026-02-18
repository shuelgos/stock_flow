from django.db import models
from django.db.models import Sum
from django.core.exceptions import ValidationError


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    minimum_stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def current_stock(self):
        
        total_in = self.movements.filter(movement_type='IN').aggregate(
            total= Sum('quantity')
        )['total'] or 0
        
        total_out= self.movements.filter(movement_type='OUT').aggregate(
            total=Sum('quantity')
        )['total'] or 0
        
        return total_in - total_out
        
            
    
class StockMovement (models.Model):
        
    MOVEMENT_TYPES=[
        ('IN', 'Entrada'),
        ('OUT', 'Salida')
    ]
        
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='movements')
    quantity = models.IntegerField()
    movement_type= models.CharField(max_length=3,choices=MOVEMENT_TYPES)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def save(self,*args,**kwargs):
        if self.movements == 'OUT':
            if self.quantity>self.product.current_stock:
                raise ValidationError ("No hay suficiente stock para esta salida")
        super().save(*args,**kwargs)    
            
        
    def __str__(self):
        return f"{self.product.name} - {self.movement_type} - {self.quantity}"
        