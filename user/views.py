from django.shortcuts import render
from rest_framework import views, status, response
from user import serializers


# Create your views here.

class UserRegistrationAPIView(views.APIView):
    def post(self, request):
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({"detail": "User created."}, status=status.HTTP_200_OK)
