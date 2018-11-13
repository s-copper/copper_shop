from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='ProductDetail'),
    url(r'^$', views.product_list, name='ProductList'),
]
