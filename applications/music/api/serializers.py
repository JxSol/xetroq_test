from typing import OrderedDict

from rest_framework import serializers

from ..models import AlbumTrack, Performer, Album, Track


class PerformerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Performer."""

    class Meta:
        model = Performer
        fields = (
            'id',
            'name',
        )


class TrackSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Track."""

    class Meta:
        model = Track
        fields = (
            'id',
            'title',
        )


class AlbumTrackSerializer(serializers.ModelSerializer):
    """Сериализатор для модели AlbumTrack."""
    title = serializers.CharField(source='track.title', read_only=True)

    class Meta:
        model = AlbumTrack
        fields = (
            'track',
            'title',
            'track_position',
        )


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Album."""
    album_tracks = AlbumTrackSerializer(many=True, required=False)

    class Meta:
        model = Album
        fields = (
            'id',
            'release_year',
            'performer',
            'album_tracks',
        )


    def create(self, validated_data: OrderedDict) -> Album:
        """Логика добавления album_tracks."""
        tracks_data = validated_data.pop('album_tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            AlbumTrack.objects.create(album=album, **track_data)
        return album

    def update(self, instance: Album, validated_data: OrderedDict) -> Album:
        """Логика обновления album_tracks."""
        tracks_data = validated_data.pop('album_tracks')
        album_tracks = instance.album_tracks

        # Обновляем Album
        instance.release_year = validated_data.get(
            'release_year',
            instance.release_year,
        )
        instance.performer = validated_data.get(
            'performer',
            instance.performer,
        )
        instance.save()

        # Для каждой песни...
        for track_data in tracks_data:
            album_track = album_tracks.filter(
                track_position=track_data.get('track_position'),
            )
            # ...обновляем связь AlbumTrack...
            if album_track.exists():
                album_track.update(track=track_data.get('track'))
            # ...или создаём новую
            else:
                AlbumTrack(
                    album=instance,
                    track=track_data.get('track'),
                    track_position=track_data.get('track_position'),
                ).save()

        return instance
