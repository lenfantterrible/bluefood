from account.forms import LoginForm
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = 'account'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/adresses', views.get_addresses, name='addresses'),
    path('profile/edit/address/<int:id>', views.edit_address, name='edit-address'),
    path('profile/add/address', views.add_address, name='add-address'),

    path('logout/', views.log_out, name='logout'),
    path('login/', LoginView.as_view(template_name='account/login.html',form_class=LoginForm, redirect_authenticated_user=True), name='login'),
    path('register/', views.UserCreationView.as_view(), name='register'),
    path('orders/', views.order_list, name='orders'),



]
