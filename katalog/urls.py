from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kopi/<int:pk>/', views.detail_kopi, name='detail_kopi'),
    path('tambah/', views.tambah_kopi, name='tambah_kopi'),
    path('edit/<int:pk>/', views.edit_kopi, name='edit_kopi'),
    path('hapus/<int:pk>/', views.hapus_kopi, name='hapus_kopi'),
]
