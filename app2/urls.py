from django.urls import path
from app2.views import *
app_name='WC2023'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('shami/',shami,name='shami.html'),
]