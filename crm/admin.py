from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


# Register your models here.
class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_dt', 'order_name', 'order_phone')


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
