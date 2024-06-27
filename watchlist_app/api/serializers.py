from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'active']

    def create(self, validated_data):
        """
        When is POST it will jump here
        Create and return a new Movie instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        When is PUT it will jump here
        Update and return an existing Movie instance, given the validated data.

        Args:
            instance: old data value
            validated_data : new data value
        """
        return super().update(instance, validated_data)

    def validate(self, data):
        """
        This function will apply validation to the entire object.
        """
        if data['name'] == data['description']:
            raise serializers.ValidationError(
                "Title and Description are the same, should be different!")
        return data

    def validate_name(self, value):
        """
        Picks the field by the name of the validation funcion, in this case the field is name.
        validate_(field_name)
        """
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        return value


"""
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
"""
