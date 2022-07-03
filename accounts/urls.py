from django.urls import path

from accounts.views import RegistrationFormView, LoginFormView, LogoutView

urlpatterns = [
    path('registration/', RegistrationFormView.as_view(), name='registration'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]