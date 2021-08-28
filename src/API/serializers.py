from django.db.models import fields
from django.db.models.base import Model
from .models import Transcations
from rest_framework import serializers

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcations
        fields = ['transaction_type', 'transaction_currency', 'transaction_amount', 'merchant_name', 'customer_name']