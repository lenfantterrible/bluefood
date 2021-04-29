from django.urls import path 
from . import views 

app_name = 'order'

urlpatterns = [
    path('add/', views.add_order, name='add-order'),

]
