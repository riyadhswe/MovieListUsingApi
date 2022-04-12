from django.urls import path
from . import views

app_name = 'App'

urlpatterns = [
    path('', views.index,name = 'index'),
    path('action/', views.action,name = 'action'),
    path('comedy/', views.comedy,name = 'comedy'),
]