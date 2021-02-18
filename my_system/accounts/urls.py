from django.urls import path

from . import views

urlpatterns = [
  path('create_form/', views.create_form, name="create_form"),
  path('create_view/', views.create_view, name="create_view"),

  path('login_form/', views.login_form, name="login_form"),
  path('login_view/', views.login_view, name="login_view"),

  path('logout/', views.logout_view, name="logout")
]