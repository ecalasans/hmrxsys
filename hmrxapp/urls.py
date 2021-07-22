from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sysLogin/', views.sysLogin, name='sysLogin'),
    path('save_filter/', views.saveFilter, name='save_filter')
]