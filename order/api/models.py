from django.db import models

# Create your models here.
class Order(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    number = models.PhoneNumberField()
    service = models.MultipleChoiceField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    place = models.ChoiceField(choices=['Salon', 'Other'])
    
    class Meta:
        db_table = 'order_form'