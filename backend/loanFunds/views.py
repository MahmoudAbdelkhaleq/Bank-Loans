from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from .models import LoanFund
from .serializers import LoanFundSerializer
# Create your views here.

class LoanFundListCreateView(generics.ListCreateAPIView):
    queryset = LoanFund.objects.all()
    serializer_class = LoanFundSerializer
    permission_classes = [permissions.IsAuthenticated]

class LoanFundDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoanFund.objects.all()
    serializer_class = LoanFundSerializer
    permission_classes = [permissions.IsAuthenticated]