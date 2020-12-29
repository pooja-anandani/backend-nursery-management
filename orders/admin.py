from django.contrib import admin

# Register your models here.

from orders.models import Cart, Orders
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    pass
class OrdersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cart,CartAdmin)
admin.site.register(Orders,OrdersAdmin)
