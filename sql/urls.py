from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('departments', views.departments, name='departments'),
  path('employees', views.employees, name='employees'),
  path('regions', views.regions, name='regions')
]