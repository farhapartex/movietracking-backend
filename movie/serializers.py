from rest_framework import serializers
from movie import models as movie_models
from user import models as user_model


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie_models.Movie
        fields = ("id", "user", "title", "year", "imdb_id", "type", "poster", "is_favorite", "is_watched")

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     validated_data['user'] = user
    #     instance = movie_models.Movie.objects.create(**validated_data)
    #     return instance
