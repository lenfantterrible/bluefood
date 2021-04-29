from store.models import City, ItemType, Seller, Item
from django.contrib import admin

@admin.register(Item)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name']

class ItemInline(admin.TabularInline):
    model = Item


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['items__name']
    inlines = [ItemInline,]


class ItemTypeInline(admin.TabularInline):
    model = ItemType

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['item_types__name']
    inlines = [ItemTypeInline]
    exclude = ('slug',)


