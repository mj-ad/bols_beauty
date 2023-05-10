from django.db import models

# Create your models here.
class Order(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    fullName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    number = models.PhoneNumberField()
    service = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'order_form'