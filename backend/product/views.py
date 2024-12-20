# from django.http import JsonResponse
# import json
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

@api_view(["GET"])
def product_view_api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()

    res = {}
    if instance:
        # res = model_to_dict(instance, fields=['id', 'title', 'content', 'price', 'sale_price'])
        res = ProductSerializer(instance).data

    return Response(res)


class ProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            ##


class ProductDestroyView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


@api_view(['GET'])
def getProductDetails(request, pk=None, *args, **kwargs):
    print(pk)
    if pk is not None:
        # queryset = Product.objects.filter(pk=pk)
        obj = get_object_or_404(Product, pk=pk)
        data = ProductSerializer(obj).data
        return Response(data)

    queryset = Product.objects.all()
    data = ProductSerializer(queryset, many=True).data
    return Response(data)

