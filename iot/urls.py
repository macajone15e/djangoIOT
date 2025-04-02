from django.urls import path
from . import views

urlpatterns = [
    # list all devices
    path('', views.device_list, name='device-list'),
    # detail view of a device
    path('<int:pk>/', views.device_detail, name='device-detail'),
]