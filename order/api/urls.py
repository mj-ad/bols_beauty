from django.urls import path
from api import views

urlpatterns = [
    path('orders', views.get, name='get'),
    path('order', views.post, name='post'),
]