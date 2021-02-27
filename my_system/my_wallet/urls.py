from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_operation/', views.new_operation_form, name='new_operation_form'),
    path('new_operation_view/', views.new_operation_view, name='new_operation_view'),
    path('list_operations/', views.list_operations, name='list_operations'),     
]