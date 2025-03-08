from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('LOAN_PROVIDER', 'Loan Provider'),
        ('LOAN_CUSTOMER', 'Loan Customer'),
        ('BANK_PERSONNEL', 'Bank Personnel'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
