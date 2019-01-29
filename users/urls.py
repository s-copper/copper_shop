from django.conf.urls import url
from django.urls import reverse, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^create/$', views.create_user, name='create_user'),
    url(r'^profile/info/(?P<userid>[-\d]+)/$', views.profile, name='profile'),
    url(r'^profile/info/edit/change_password/$', views.change_password, name='change_password'),
    url(r'^profile/info/edit/change_email/$', views.change_email, name='change_email'),
    url(r'^profile/info/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/logout/$', views.logout_view, name='logout_view'),
    url(r'^profile/login/$', views.login_view, name='login_view'),
    url(r'^profile/password_reset/$', auth_views.PasswordResetView.as_view(
        template_name='users/reset_password_form.html',
        email_template_name='users/reset_password_email.html',
        subject_template_name='users/reset_password_subject.txt',
        success_url=reverse_lazy('users:password_reset_done'),
    ), name='password_reset'),
    url(r'^profile/password_reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='users/reset_password_done.html'
    ), name='password_reset_done'),
    url(r'^profile/password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/reset_password_confirm.html',
            success_url=reverse_lazy('users:password_reset_complete')
        ), name='password_reset_confirm'),
    url(r'^profile/password_reset/complete/$', views.my_reset_password_complete, name='password_reset_complete'),
]
