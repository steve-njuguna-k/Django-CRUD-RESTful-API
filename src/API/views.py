from rest_framework.response import Response
from .models import Transactions
from .serializers import TransactionsSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def AllTransactions(request):
    transactions = Transactions.objects.all()
    serializer = TransactionsSerializer(transactions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def TransactionsDetails(request, id):
    transactions = Transactions.objects.get(id=id)
    serializer = TransactionsSerializer(transactions, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddTransactions(request):
    serializer = TransactionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def UpdateTransactionsDetails(request, id):
    transactions = Transactions.objects.get(id=id)
    serializer = TransactionsSerializer(data=request.data, instance=transactions)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteTransaction(request, id):
    transactions = Transactions.objects.get(id=id)
    transactions.delete()
    return Response({'Transaction Record Successfully Deleted!'})