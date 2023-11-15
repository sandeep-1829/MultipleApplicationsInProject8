from django.urls import path
from app1.views import *
app_name = 'WC2023'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('bumrah/',bumrah,name='bumrah'),
]