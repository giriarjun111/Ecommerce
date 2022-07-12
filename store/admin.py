from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

class ShippingAddressInline(admin.StackedInline):
    model = ShippingAddress
    extra = 0

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'digital', 'category']
    list_filter = ['price', 'digital']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', "show_username", 'date_added']
    readonly_fields = ['date_added']

    def show_username(self, obj):
        myuser = Customer.objects.get(name=obj)
        return myuser

    show_username.short_description = 'Person'


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['order', 'address', 'date_added']

class CustomerAdmim(admin.ModelAdmin):
    inlines = [OrderItemInline, ShippingAddressInline]



# Register your models here.
admin.site.register(Customer, CustomerAdmim)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Product, ProductAdmin)




