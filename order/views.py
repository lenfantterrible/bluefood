from django.http.response import Http404
from order.models import Entry, Order
from store.models import Item, Seller
from account.models import Address
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket 

@login_required(login_url='/account/login/')
def add_order(request):
    if request.method == 'POST':
        basket = Basket(request)
        
        if basket.is_empty():
            error = 'Basket is empty'
            return render(request, 'order/add_order.html', {'order': None, 'error': error})
        if not request.POST.get('address'):
            error = 'Select Address'
            return render(request, 'order/add_order.html', {'order': None, 'error': error})
        
        seller  = get_object_or_404(Seller, slug=request.session['seller'])
        address = get_object_or_404(Address, id=request.POST.get('address'))
        order = Order(user=request.user, seller=seller, address=address)
        order.save()
        for item,info in basket.basket.items():
            try:
                item = seller.items.get(name=item)
            except Item.DoesNotExist:
                return Http404
            
            entry = Entry(item=item, order=order, quantity=info['qty'])
            entry.save()
        
        basket.clean()
        return render(request, 'order/add_order.html', {'order': order, 'error': None})
    else:
        addresses = request.user.addresses.all()
        return render(request, 'order/finalize_order.html', {'addresses': addresses})



