from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.filters import (
    SearchFilter, OrderingFilter)

from .serializers import (
    CategoriesSerializer, SubCategorySerializers, ProductsSerializers
)

from .models import Categories, SubCategories, Product


class GetCategories(generics.ListAPIView):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()


class GetSubCategories(generics.ListAPIView):
    serializer_class = SubCategorySerializers
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['category__name']
    queryset = SubCategories.objects.all()


class GetProducts(generics.ListAPIView):
    serializer_class = ProductsSerializers
    queryset = Product.objects.all()

    def filter_queryset(self, queryset):
        if 'category' in self.request.query_params:
            queryset = queryset.filter(subcategory__category__name=self.request.query_params['category'])
        elif 'subcategory' in self.request.query_params:
            queryset = queryset.filter(subcategory__name=self.request.query_params['subcategory'])
        return queryset
