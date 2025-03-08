from rest_framework import serializers
from .models import Loan, LoanProduct
from users.models import User

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'loaner', 'LoanProduct', 'created_at']


    def validate_user(self, value):
        # Ensure the user is a LOAN_CUSTOMER
        if value.role != 'LOAN_CUSTOMER':
            raise serializers.ValidationError("Loans can only be associated with LOAN_CUSTOMER users.")
        return value


class LoanProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProduct
        fields = ['id', 'amount', 'term', 'interest_rate', 'created_at', 'created_by']

    def validate_user(self, value):
        # Ensure the user is a LOAN_CUSTOMER
        if value.role != 'BANK_PERSONNEL':
            raise serializers.ValidationError("Loan products can only be associated with BANK_PERSONNEL users.")
        return value