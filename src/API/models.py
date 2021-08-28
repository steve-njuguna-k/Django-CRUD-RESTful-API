from django.db import models
from django.db.models.fields import UUIDField
import uuid

TRANSACTION_TYPE = [
    ('Debit', ('Debit')),
    ('Credit', ('Credit')),
]

CURRENCY = [
    ('KSH', ('KSH')),
    ('TSH', ('TSH')),
    ('USH', ('USH'))
]

# Create your models here.
class Transactions(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False, max_length=50)
    type = models.CharField(choices=TRANSACTION_TYPE, max_length=50)
    currency = models.CharField(choices=CURRENCY, max_length=50)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    merchant_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False, max_length=50)
    merchant_name = models.CharField(max_length=50)
    customer_id = models.CharField(default=uuid.uuid4, unique=True, db_index=True, editable=False, max_length=50)
    customer_name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.transaction_id)

    class Meta:
        verbose_name_plural = 'Transactions'