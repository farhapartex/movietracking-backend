from django.shortcuts import render
from rest_framework import views, status, response, permissions
from movie import serializers


# Create your views here.

class CreateMovieInfoAPiView(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        requested_data = request.data
        requested_data["user"] = request.user.id
        serializer = serializers.MovieCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({"detail": "Movie data added."}, status=status.HTTP_200_OK)