# Generated by Django 3.2.6 on 2021-08-28 12:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=50)),
                ('transaction_currency', models.CharField(choices=[('KSH', 'KSH'), ('TSH', 'TSH'), ('USH', 'USH')], max_length=50)),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('merchant_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('merchant_name', models.CharField(max_length=50)),
                ('customer_id', models.CharField(db_index=True, default=uuid.uuid4, editable=False, max_length=50, unique=True)),
                ('customer_name', models.CharField(max_length=50)),
                ('transaction_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]
