from django.db import models

# Create your models here.

class Payment_info(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    payment_id = models.CharField(max_length=264, blank=True, null=True)
    order_id = models.CharField(max_length=264, blank=True, null=True)
    amount = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)