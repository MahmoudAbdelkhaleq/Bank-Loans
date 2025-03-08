from django.db import models
from users.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q


# Create your models here.
class LoanFund(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loan_funds')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Ensure the user is a LOAN_PROVIDER
        if self.user.role != 'LOAN_PROVIDER':
            raise ValidationError("Loan funds can only be associated with LOAN_PROVIDER users.")
        super().clean()

    def __str__(self):
        return f"Loan Fund {self.id} - {self.user.username}"