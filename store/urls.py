from django.urls import path 
from . import views 


app_name = 'store'

urlpatterns = [

    path('', views.home_page, name='home_page'),
    path('restaurants/<str:city>', views.restaurant_list, name='restaurant_list'),
    path('menu/<slug:slug>', views.menu, name='menu'),
    path('menu/seller/<slug:slug>/type/<int:id>', views.get_items, name='get_items'),

]