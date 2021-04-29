from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from django.utils.translation import gettext as _
import uuid 
from uuslug import uuslug 

class Item(models.Model):

    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False,
         unique=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    item_type = models.ForeignKey("store.ItemType", on_delete=models.CASCADE, related_name='items')
    seller = models.ForeignKey("store.Seller", null=True, on_delete=models.CASCADE, related_name='items')
    image = models.ImageField(upload_to='products/', default='download.joeg')

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Item_detail", kwargs={"pk": self.pk})

class ItemType(models.Model):

    name = models.CharField(max_length=20)
    seller = models.ForeignKey("store.Seller", on_delete=models.CASCADE, related_name='item_types')

    class Meta:
        verbose_name = _("ItemType")
        verbose_name_plural = _("ItemTypes")

    def __str__(self):
        return self.name

class City(models.Model):

    name = models.CharField(max_length=20, unique=True)


    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("city_detail", kwargs={"pk": self.pk})


class Seller(models.Model):

    name = models.CharField(max_length=35)
    city = models.ForeignKey(City, related_name='sellers', on_delete=models.CASCADE)
    address = models.TextField(max_length=150)
    slug = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='logos/', default='logos/download.jpeg')


    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:menu", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
         self.slug = uuslug(self.name, instance=self)
         super(Seller, self).save(*args, **kwargs)



