from rest_framework import serializers

from .models import Categories, SubCategories, Product


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ('name',)


class SubCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = SubCategories
        fields = ('name',)


class ProductsSerializers(serializers.ModelSerializer):
    category = serializers.ReadOnlyField()
    sub_category = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ('name', 'category', 'sub_category')
