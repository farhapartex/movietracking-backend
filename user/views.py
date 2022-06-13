from django.shortcuts import render
from rest_framework import views, status, response
from rest_framework_simplejwt import views as jwt_views
from user import serializers


# Create your views here.
class UserAuthTokenView(jwt_views.TokenObtainPairView):
    serializer_class = serializers.UserAuthTokenSerializer


class UserRegistrationAPIView(views.APIView):
    def post(self, request):
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({"detail": "User created."}, status=status.HTTP_200_OK)
