from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from apps.shop.serializers import ProductSerializer
from apps.shop.models import Product


@api_view(["POST"])
def product_apiview(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT", "PATCH"])
def product_update_apiview(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(
        instance=product, data=request.data, many=False, partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(
            {"message": "You product data invalid, please try again"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def product_fetch_apiview(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def product_delete_apiview(request, pk):
    try:
        Product.objects.get(pk=pk).delete()
        return Response(
            {"message": "Product successfully Delete"},
            status=status.HTTP_204_NO_CONTENT,
        )
    except Exception as e:
        return Response(
            {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )
