from django.urls import path
from .import views

urlpatterns=[
    path('',views.weather,name='index'),
    path('delete/<city_name>', views.del_city, name="del_city")
]