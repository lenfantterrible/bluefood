from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from .models import City, Seller 
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.core import serializers
from basket.basket import Basket

def home_page(request):
    return render(request, 'base.html')

def restaurant_list(request, city):
    city1 = get_object_or_404(City, name__iexact=city.lower())
    sellers = city1.sellers.all()
    paginator = Paginator(sellers, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store/restaurant_list.html', {'page_obj': page_obj})

def menu(request, slug):
    seller = get_object_or_404(Seller, slug=slug)
    return render(request, 'store/menu.html', {'seller': seller})

def get_items(request, slug, id):
    seller = get_object_or_404(Seller, slug=slug)
    item_type = seller.item_types.get(id=id)
    response = serializers.serialize('json', item_type.items.filter(available=True))
    return HttpResponse(response, content_type="application/json")
