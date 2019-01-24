from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.create_user, name='create_user'),
    url(r'^profile/info/(?P<userid>[-\d]+)/$', views.profile, name='profile'),
    url(r'^profile/logout/$', views.logout_view, name='logout_view'),
    url(r'^profile/login/$', views.login_view, name='login_view')

]
