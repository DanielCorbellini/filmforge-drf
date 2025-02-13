from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlataform


class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id', 'name', 'description', 'active']
        # exclude = ['name']

    def create(self, validated_data):
        """
        When is POST it will jump here
        Create and return a new Movie instance, given the validated data.
        """
        return WatchList.objects.create(**validated_data)

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
        if data['title'] == data['storyline']:
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

    def get_len_name(self, object):
        """
        This is a read-only field. It gets its value by calling a method on the serializer class it is attached to.
        It can be used to add any sort of data to the serialized representation of your object.
        """
        length = len(object.title)
        return length


class StreamPlataformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True) Mostra o que retorna na função __str__
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  Mostra só a chave primária
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')

    class Meta:
        model = StreamPlataform
        fields = "__all__"
