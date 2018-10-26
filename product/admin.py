from django.contrib import admin

from .models import Categories, SubCategories, Product


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "created")
    search_fields = ("name",)


@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ("category", "name", "created")
    search_fields = ("category__name", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("subcategory", "name", "created")
    search_fields = ("subcategory__name", "name")
