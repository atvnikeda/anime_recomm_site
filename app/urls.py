from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^home/',views.home,name='home'),
    url(r'^anime_regis/',views.anime_regis,name='anime_regis'),
    url(r'^anime_recomm/',views.anime_recomm,name='anime_recomm'),
]
