from rest_framework import permissions

class IsLoanProvider(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'LOAN_PROVIDER'

class IsLoanCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'LOAN_CUSTOMER'

class IsBankPersonnel(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'BANK_PERSONNEL'