from django.urls import path
from . import views
urlpatterns = [
    path('demo1', views.demo1),
    path("login",views.login)
]