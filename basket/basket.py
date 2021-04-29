from decimal import Decimal
from store.models import Item


class Basket():
    
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        if 'seller' not in request.session:
            self.session['seller'] = {}
        self.basket = basket

    def add(self, item, qty):
        seller = item.item_type.seller 
        
        if 'seller' not in self.session:
            self.session['seller'] = seller.slug 
        
        elif(self.session['seller'] != seller.slug):
            self.session['seller'] = seller.slug 
            self.basket = self.session['skey'] = {}
        
        if item.name not in self.basket:
            self.basket[item.name] = {'price': str(item.price), 'qty': int(qty)}

        self.session.modified = True

    def delete(self, item_name):
        self.basket.pop(str(item_name))
        self.session.modified = True

    def clean(self):
        self.basket.clear()
        self.session['seller'] = None

    def update(self, item_name, qty):
        self.basket[item_name]['qty'] += qty 
        self.session.modified = True
        
    def is_empty(self):
        return not bool(self.basket)
        
    def __len__(self):
        return sum(product['qty'] for product in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])*item['qty'] for item in self.basket.values())

