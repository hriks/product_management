# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import views
from django.shortcuts import render


class Dashboard(views.View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
