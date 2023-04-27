from django.urls import path
from .views import VRegister, close_session, open_session

urlpatterns = [
    path('', VRegister.as_view(), name="Register"),
    path('close_session', close_session, name="Logout"),
    path('login',open_session, name="Login"),
]