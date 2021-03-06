from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='CartAdd'),
    url(r'^change/$', views.cart_change_quantity, name='cart_change_quantity'),
    url(r'^', views.cart_detail, name='CartDetail'),
]
