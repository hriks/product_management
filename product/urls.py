from django.conf.urls import url
import views
import apis

urlpatterns = [
    url(r'^categories$', apis.GetCategories.as_view()),
    url(r'^subcategories$', apis.GetSubCategories.as_view()),
    url(r'^products$', apis.GetProduct.as_view()),
#    url(r'^blog/(?P<id>[A-Za-z_0-9\-]+)$', views.BlogDetails.as_view()),
    #url(r'^', views.BaseTemplate.as_view()),
]
