from rest_framework import serializers
from .models import Transactions



class TransactionsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Transactions
        # fields = [
        #     "title",
        #     "amount",
        #     # "transaction_type",
        # ]

        fields = '__all__'
        # exclude = ['transaction_type','amount']