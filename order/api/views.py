from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
@api_view(['GET'])

def get(request, *args, **kwargs):
    """
    List and create order data
    """
    orders = Order.objects.all().order_by('date')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post(request, *args, **kwargs):
    serialize = OrderSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response({
            'data': serialize.data,
            'message': 'Successful'
            }, status=status.HTTP_201_CREATED)
    else:
        default = serialize.errors
        error = {}
        for field_name, field_errors in default.items():
            error[field_name] = field_errors[0]
        return Response({
            'message': 'Bad Request',
            'error': error}, status=status.HTTP_400_BAD_REQUEST)