from django.http.response import JsonResponse
from .basket import Basket 

def basket(request):
    return {'basket': Basket(request).basket}