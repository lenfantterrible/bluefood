from account.forms import RegistrationForm
from django.views.generic.edit import CreateView
from store.models import City
from account.models import Address, MyUser
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django_email_verification import send_email
from order.models import Order
from django.views.generic.list import ListView
from django.core.paginator import Paginator


@login_required(login_url='/account/login/')
def profile(request):

    return render(request, 'account/profile.html')


@login_required(login_url='/account/login/')
def get_addresses(request):
    addresses = request.user.addresses.all()
    return render(request, 'account/addresses.html', {'addresses': addresses})

@login_required(login_url='/account/login/')
def edit_address(request, id):
    try:
        address = request.user.addresses.get(id=id)

    except Address.DoesNotExist:
        raise Http404()
    
    if request.method == 'POST':
        address.address  = request.POST['address'];
        address.city = get_object_or_404(City, id=request.POST['city'])
        address.save()
        return redirect('account:addresses')
    else:
        return render(request, 'account/edit_address.html', {'address': address})

@login_required(login_url='/account/login/')
def add_address(request):
    
    if request.method == 'POST':
        address = Address()
        address.user = request.user
        address.address  = request.POST['address'];
        address.city = get_object_or_404(City, id=request.POST['city'])
        address.save()
        return redirect('account:addresses')
    else:
        return render(request, 'account/add_address.html')


def log_out(request):
    logout(request)
    return redirect('/account/login')


class UserCreationView(CreateView):
    model = MyUser
    form_class = RegistrationForm
    template_name = 'account/register.html'
    success_url = "/account/profile"

    def form_valid(self, form):
        user = form.save()
        returnVal = super(UserCreationView, self).form_valid(form)
        send_email(user)
        return returnVal


def order_list(request):
    orders = request.user.orders.all()
    paginator = Paginator(orders, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'account/order_list.html', {'orders': orders, 'page_obj': page_obj})