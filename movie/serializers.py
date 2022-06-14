from rest_framework import serializers
from movie import models as movie_models
from user import models as user_model


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie_models.Movie
        fields = ("id", "user", "title", "year", "imdb_id", "type", "poster", "is_favorite", "is_watched")

    def create(self, validated_data):
        imdb_id = validated_data["imdb_id"]
        instance = movie_models.Movie.get_instance({"imdb_id": imdb_id})
        if instance is None:
            return movie_models.Movie.objects.create(**validated_data)
        instance.title = validated_data["title"]
        instance.poster = validated_data["poster"]
        instance.is_favorite = validated_data.get("is_favorite", False) if instance.is_favorite is False else instance.is_favorite
        instance.is_watched = validated_data.get("is_watched", False) if instance.is_watched is False else instance.is_watched
        instance.save()

        return instance
