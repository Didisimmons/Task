from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('result/<sensor_id>', views.result, name='result'),
    path('delete/<sensor_id>', views.delete_sensor,
         name='delete_sensor'),
]
