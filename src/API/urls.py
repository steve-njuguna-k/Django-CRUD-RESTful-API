from . import views
from django.urls import path

urlpatterns = [
    path('api/v1', views.Overview, name="Overview"),
    path('api/v1/transactions', views.AllTransactions, name="AllTransactions"),
    path('api/v1/transactions/<int:id>', views.TransactionsDetails, name="TransactionsDetails"),
    path('api/v1/transactions/create', views.AddTransactions, name="AddTransactions"),
    path('api/v1/transactions/update/<int:id>', views.UpdateTransactionDetails, name="UpdateTransactionDetails"),
    path('api/v1/transactions/delete/<int:id>', views.DeleteTransaction, name="DeleteTransaction"),
]
