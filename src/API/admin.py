from django.contrib import admin
from .models import Transactions

# Register your models here.
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'type', 'currency', 'amount', 'merchant_name', 'customer_name', 'timestamp')
    search_fields = ['merchant_name', 'customer_name', 'amount']
    ordering = ['merchant_name', 'customer_name']
    readonly_fields=('transaction_id', 'merchant_id', 'customer_id', 'timestamp')

admin.site.register(Transactions, TransactionsAdmin)