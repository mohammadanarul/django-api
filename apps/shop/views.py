from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from apps.shop.serializers import ProductSerializer
from apps.shop.models import Product


@api_view(["GET"])
def product_apiview(request):
    objects = Product.objects.all()
    serializer = ProductSerializer(objects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
