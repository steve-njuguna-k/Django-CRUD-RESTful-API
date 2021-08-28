from django.db.models import fields
from django.db.models.base import Model
from .models import Transactions
from rest_framework import serializers

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'