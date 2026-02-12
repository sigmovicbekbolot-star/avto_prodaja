from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list_view, name='home'),
    path('api/', views.CarListAPIView.as_view(), name='car-api'),
    path('add-car/', views.add_car_view, name='add-car'),
    path('register/', views.register_view, name='register'),
]