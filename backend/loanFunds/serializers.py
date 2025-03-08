from rest_framework import serializers
from .models import LoanFund
from users.models import User

class LoanFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanFund
        fields = ['id', 'user', 'amount', 'created_at']

    def validate_user(self, value):
        # Ensure the user is a LOAN_PROVIDER
        if value.role != 'LOAN_PROVIDER':
            raise serializers.ValidationError("Loan funds can only be associated with LOAN_PROVIDER users.")
        return value