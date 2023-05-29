from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Order(models.Model):
    PLACE_CHOICES = (('Salon', 'Salon'), ('Other', 'Other'))
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    number = PhoneNumberField()
    service = models.JSONField(max_length=100)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    place = models.CharField(choices=PLACE_CHOICES, max_length=20)
    
    class Meta:
        db_table = 'order_form'