from django.urls import path
from . import views

urlpatterns = [
    # list all devices
    path('devices/', views.DeviceList.as_view(), name='device-list'),
    # detail view of a device
    path('devices/<int:pk>/', views.DeviceDetail.as_view(), name='device-detail'),
]