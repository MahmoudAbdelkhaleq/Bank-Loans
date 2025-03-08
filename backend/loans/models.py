from django.db import models
from users.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Loan(models.Model):
    loaner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loaner', default=None)
    LoanProduct = models.ForeignKey('LoanProduct', on_delete=models.CASCADE, related_name='loans', default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Ensure the user is a LOAN_CUSTOMER
        if self.user.role != 'LOAN_CUSTOMER':
            raise ValidationError("Loans can only be associated with LOAN_CUSTOMER users.")
        super().clean()

    def __str__(self):
        return f"Loan {self.id} - {self.user.username}"
    

class LoanProduct(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.PositiveIntegerField()  # Loan term in months
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='creator', default=None)

    def clean(self):
        # Ensure the user is a LOAN_CUSTOMER
        if self.user.role != 'BANK_PERSONNEL':
            raise ValidationError("Loan products can only be associated with BANK_PERSONNEL users.")
        super().clean()

    def __str__(self):
        return f"Loan Product {self.id}"