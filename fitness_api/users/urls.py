from django.urls import path
from .views import LoginView, RegisterView, CurrentUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('register', RegisterView.as_view(), name='user-register-no-slash'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('login', LoginView.as_view(), name='user-login-no-slash'),
    path('me/', CurrentUserView.as_view(), name='user-me'),
    path('me', CurrentUserView.as_view(), name='user-me-no-slash'),
]
