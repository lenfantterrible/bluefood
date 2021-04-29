from store.models import Item, Seller
from django.db import models
from django.urls.base import reverse
from django.utils.translation import gettext as _

class Order(models.Model):

    user = models.ForeignKey("account.MyUser", on_delete=models.CASCADE, related_name='orders')
    seller = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    address = models.ForeignKey("account.Address", null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
    
    def __str__(self):
        return "{} ordered from {}.".format(self.user, self.seller)


    def get_absolute_url(self):
        return reverse("order:order_detail", kwargs={"slug": self.slug})
    
    def get_total_price(self):
        return sum(item.price for item in self.items.all())

class Entry(models.Model):
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='entries')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.item.name)
