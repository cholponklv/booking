from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import CreateAdminView, SendToRecoverPassword, VerificationPasswordCodeAPIView, NewPasswordView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create_admin/', CreateAdminView.as_view(), name = 'create_admin'),
    path('send_email_token/', SendToRecoverPassword.as_view(), name = 'send_ps'),
    path('check_email_token/', VerificationPasswordCodeAPIView.as_view(), name = 'check_ps'),
    path('new_password/', NewPasswordView.as_view(), name='new_password' ),
    ]