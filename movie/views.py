from django.shortcuts import render
from rest_framework import views, status, response, permissions
from movie import serializers, models


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


class MovieListAPiView(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        if "q" not in request.GET or request.GET["q"] not in ["favorite", "watched"]:
            return response.Response({"detail": "Missing query param"}, status=status.HTTP_400_BAD_REQUEST)
        query = request.GET["q"]
        queryset = models.Movie.objects.filter(user=request.user)
        queryset = queryset.filter(is_favorite=True) if query == "favorite" else queryset.filter(is_watched=True)

        data = serializers.MovieCreateSerializer(queryset, many=True).data
        return response.Response(data, status=status.HTTP_200_OK)