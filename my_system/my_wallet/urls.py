from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_form, name="login_form"),
    # path('login_view/', views.login_view, name="login_view"),
    # path('logout/', views.logout_view, name="logout_view"),        
]