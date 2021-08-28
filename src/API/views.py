from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import Transcations
from .serializers import TransactionsSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def ListTransaction(request):
    transactions = Transcations.objects.all()
    serializer = TransactionsSerializer(transactions, many=True)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def TransactionsDetails(request, id):
    transactions = Transcations.objects.get(id=id)
    serializer = TransactionsSerializer(transactions, many=False)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def AddTransactions(request):
    serializer = TransactionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data)

@api_view(['PUT'])
def UpdateTransactionsDetails(request, id):
    transactions = Transcations.objects.get(id=id)
    serializer = TransactionsSerializer(data=request.data, instance=transactions)

    if serializer.is_valid():
        serializer.save()

    return JsonResponse(serializer.data)

@api_view(['DELETE'])
def DeleteTransactions(request, id):
    transactions = Transcations.objects.get(id=id)
    transactions.delete()
    return Response({'Transaction Record Successfully Deleted!'})