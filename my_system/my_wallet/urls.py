from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_operation/', views.new_operation_form, name='new_operation_form'),
    path('new_operation_view/', views.new_operation_view, name='new_operation_view'),
    path('list_same_share_operations_form/', views.list_same_share_operations_form, name='list_same_share_operations_form'),
    # path('login/', views.login_form, name="login_form"),
    # path('login_view/', views.login_view, name="login_view"),
    # path('logout/', views.logout_view, name="logout_view"),        
]