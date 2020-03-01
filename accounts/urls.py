from django.conf.urls import include,url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^signin/',auth_views.LoginView.as_view(template_name='signin.html'),name='signin'),
    url(r'^signup/',views.signup,name='signup'),
]
