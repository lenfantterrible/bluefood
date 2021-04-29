from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from store.models import Item, ItemType
from django.core import serializers
from .basket import Basket


def basket_summary(request):
    return render(request, 'store/basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        item_name = request.POST.get('item_name')
        item_qty = int(request.POST.get('qty'))
        item_type = get_object_or_404(ItemType, id=request.POST.get('item_type'))
        try:
            item = item_type.items.get(name=item_name)
        except Item.DoesNotExist:
            return Http404()

        basket.add(item, item_qty)

        return JsonResponse({'data': basket.basket})

def get_basket(request, seller):
    basket = Basket(request)

    if(basket.session['seller'] != seller):
        return JsonResponse({'data': None})
    
    return JsonResponse({'data': basket.basket})

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        item_name = request.POST.get('item_name')
        basket.delete(item_name)
        return JsonResponse({'data': basket.basket})


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        item_name = request.POST.get('item_name')
        qty = request.POST.get('qty')
        
        if int(basket.basket[item_name]['qty']) + int(qty) <= 0: 
            return basket_delete(request)

        basket.update(item_name, int(qty))

        return JsonResponse({'data': basket.basket})

