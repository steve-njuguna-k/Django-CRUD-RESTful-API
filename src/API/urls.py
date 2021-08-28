from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListTransactions, name="ListTransactions"),
    path('api/transactions/<int:id>', views.TransactionsDetails, name="TransactionsDetails"),
    path('api/transactions/create', views.AddTransactions, name="AddTransactions"),
    path('api/transactions/update/<int:id>', views.UpdateTransactionsDetails, name="UpdateTransactionsDetails"),
    path('api/transactions/delete/<int:id>', views.DeleteTransaction, name="DeleteTransaction"),
]
