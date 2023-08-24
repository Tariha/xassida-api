from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from allauth.account.views import ConfirmEmailView
from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path("users/", UserDetailsView.as_view(), name="rest_user_details"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path("verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
            name='account_confirm_email',),
    path('account-email-verification-sent/', VerifyEmailView.as_view(),
         name='account_email_verification_sent',),
]
