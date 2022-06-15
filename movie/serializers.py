from django.conf import settings
from rest_framework import serializers, status
from movie import rapid_api, models as movie_models
import time


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie_models.Movie
        fields = ("id", "user", "title", "year", "imdb_id", "type", "poster", "is_favorite", "is_watched", "rated", "runtime", "genre", "director", "writer", "actors", "plot", "language", "country", "awards", "released")

    def add_movie_util_data(self, movie_data:dict, instance: movie_models.Movie):
        instance.rated = movie_data.get("Rated", "")
        instance.runtime = movie_data.get("Runtime", "")
        instance.genre = movie_data.get("Genre", "")
        instance.director = movie_data.get("Director", "")
        instance.writer = movie_data.get("Writer", "")
        instance.actors = movie_data.get("Actors", "")
        instance.plot = movie_data.get("Plot", "")
        instance.language = movie_data.get("Language", "")
        instance.country = movie_data.get("Country", "")
        instance.awards = movie_data.get("Awards", "")
        instance.released = movie_data.get("Released", "")

    def create(self, validated_data):
        imdb_id = validated_data["imdb_id"]
        user = validated_data["user"]
        res_status, movie_data = rapid_api.search_movie_by_imdb_id(imdb_id, settings.RAPID_API_KEY)
        instance = movie_models.Movie.get_instance({"imdb_id": imdb_id, "user": user})
        if instance is None:
            movie_instance = movie_models.Movie.objects.create(**validated_data)
            if res_status == status.HTTP_200_OK and movie_data:
                self.add_movie_util_data(movie_data, movie_instance)
                movie_instance.save()
                return movie_instance

        instance.title = validated_data["title"]
        instance.poster = validated_data["poster"]
        instance.is_favorite = validated_data.get("is_favorite", False) if instance.is_favorite is False else instance.is_favorite
        instance.is_watched = validated_data.get("is_watched", False) if instance.is_watched is False else instance.is_watched

        res_status, movie_data = rapid_api.search_movie_by_imdb_id(imdb_id, settings.RAPID_API_KEY)

        if res_status == status.HTTP_200_OK and movie_data:
            self.add_movie_util_data(movie_data, instance)

        instance.save()

        return instance


class MovieSearchSerializer(serializers.Serializer):
    title = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass