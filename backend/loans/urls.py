from django.urls import path
from .views import *

urlpatterns = [
    path('', LoanListCreateView.as_view(), name='loan-list-create'),
    path('<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
    path('update-loan/<int:pk>/', UpdateLoanView.as_view(), name='approve-loan'),
]