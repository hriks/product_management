from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import (
    CategoriesSerializer, SubCategorySerializers, ProductsSerializers,
    ProductCreateSerializer
)

from .models import Categories, SubCategories, Product


class GetCategories(generics.ListAPIView):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        if 'subcategory' in request.query_params:
            queryset = [SubCategories.objects.get(name=request.query_params['subcategory']).category]
        return Response([
            category['name'] for category in CategoriesSerializer(
                queryset, many=True).data
        ], status=status.HTTP_200_OK)


class GetSubCategories(generics.ListAPIView):
    serializer_class = SubCategorySerializers
    queryset = SubCategories.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        if 'category' in request.query_params:
            queryset = queryset.filter(category__name=request.query_params['category'])
        return Response([
            subcategory['name'] for subcategory in SubCategorySerializers(
                queryset, many=True).data
        ], status=status.HTTP_200_OK)


class GetProducts(generics.ListCreateAPIView):
    serializer_class = ProductsSerializers
    queryset = Product.objects.all()

    def filter_queryset(self, queryset):
        if 'category' in self.request.query_params:
            queryset = queryset.filter(subcategory__category__name=self.request.query_params['category'])
        elif 'subcategory' in self.request.query_params:
            queryset = queryset.filter(subcategory__name=self.request.query_params['subcategory'])
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = ProductCreateSerializer(data=request.data)
        serializer.is_valid()
        cleaned_data = serializer.validated_data
        subcategory = SubCategories.objects.get(name=cleaned_data['subcategory'])
        Product.objects.create(subcategory=subcategory, name=cleaned_data['product'])
        return Response(ProductsSerializers(
            self.get_queryset(), many=True).data, status=status.HTTP_201_CREATED)
