from django.conf.urls import url
import views
import apis

urlpatterns = [
    url(r'^categories$', apis.GetCategories.as_view()),
    url(r'^subcategories$', apis.GetSubCategories.as_view()),
    url(r'^products/$', apis.GetProducts.as_view(), name="get_or_createProduct"),
    url(r'^', views.Dashboard.as_view()),
]
