from django.urls import path
from .views import RegisterView, LoginView, ProfileView, UserListView, UserDeleteView

urlpatterns = [
    # User registration
    path('register/', RegisterView.as_view(), name='register'),

    # User login
    path('login/', LoginView.as_view(), name='login'),

    # User profile (view/update)
    path('profile/', ProfileView.as_view(), name='profile'),

    # List all users (Bank Personnel only)
    path('users/', UserListView.as_view(), name='user-list'),

    # Delete a user (Bank Personnel only)
    path('users/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]