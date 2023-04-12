from django.urls import path

from .views import AccountLoginView, ProfileView, CustomLogutView

app_name = "account"

urlpatterns = [
    path("login/", AccountLoginView.as_view(), name="login"),
    path("logout/", CustomLogutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name='profile')
]