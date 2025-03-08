from django.urls import path
from .views import *

urlpatterns = [
    path('', LoanFundListCreateView.as_view(), name='loan-fund-list-create'),
    path('<int:pk>/', LoanFundDetailView.as_view(), name='loan-fund-detail'),
]