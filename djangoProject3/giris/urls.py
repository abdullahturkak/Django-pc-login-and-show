from django.urls import path
from . import views
from django.urls import path
from django.urls import path





urlpatterns = [
    path('', views.ilksayfa,name='ilksayfa'),
    path('ekle',views.ekle,name='ekle'),
    path('getir',views.index,name='getir'),




]
