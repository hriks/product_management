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

    def get_category(self, obj):
        return obj.name

    class Meta:
        model = Product
        fields = '__all__'
