from django.urls import path
from . import views

app_name = 'premain'

urlpatterns = [
     path('', views.index, name='index'),
]
