from __future__ import unicode_literals

from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=128)
    created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class SubCategories(models.Model):
    category = models.ForeignKey(Categories, null=True, blank=True)
    name = models.CharField(max_length=128)
    created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategories, null=True, blank=True)
    name = models.CharField(max_length=256)
    created = models.DateField(auto_now_add=True)

    @property
    def category(self):
        return self.subcategory.category

    def __unicode__(self):
        return self.name
