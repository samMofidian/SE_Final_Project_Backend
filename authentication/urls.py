from django.urls import path
from . import views
from .views import VerifyEmail

urlpatterns = [
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('register/', views.registration_views, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
]