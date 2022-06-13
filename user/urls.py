from django.urls import re_path
from user import views

urlpatterns = [
    re_path(r"^api/v1/registration/", views.UserRegistrationAPIView.as_view()),
]