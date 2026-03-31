from django.shortcuts import render
from rest_framework.response import Response
from .models import Transactions
from .serializers import TransactionsSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view()
def get_transactions(request):
    queryset = Transactions.objects.all()
    serializer = TransactionsSerializer(queryset, many=True)

    return Response({
        "data": serializer.data
    })



class TransactionAPI(APIView):
    def get(self, request):
        queryset = Transactions.objects.all()
        serializer = TransactionsSerializer(queryset, many=True)
        return Response({
            "data":serializer.data
        })
    
    def post(self, request):
        data = request.data
        serializer = TransactionsSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                "message": "problem in adding in transaction",
                "errors": serializer.errors,
            })
        serializer.save()
        return Response({
            "message": "this is a post method",
            "data": serializer.data 
        })
    
    def put(self, request):
        return Response({
            "message": "this is a put method"
        })
    
    def patch(self, request):
        data = request.data

        if not data.get('id'):
             return Response({
                "message": "problem in patching in transaction",
                "errors": "id is required",
            })
        
        transaction = Transactions.objects.get(id=data.get('id'))
        serializer = TransactionsSerializer(transaction, data=data, partial=True)
        if not serializer.is_valid():
            return Response({
                "message": "problem in patching in transaction",
                "errors": serializer.errors,
            })
        serializer.save()
        return Response({
             "message": "this is a patch method",
            "data": serializer.data 
        })
    
    def delete(self, request):
        data = request.data

        if not data.get('id'):
             return Response({
                "message": "problem in deleting the transaction",
                "errors": "id is required",
            })
        
        transaction = Transactions.objects.get(id=data.get('id')).delete()
        
        
        return Response({
             "message": "this is a delete method",
            "data": {} 
        })
