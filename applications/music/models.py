from django.db import models

from .validators import validate_past_year


class Track(models.Model):
    """Песня."""
    title = models.CharField(
        verbose_name='Название',
        max_length=50,
    )

    class Meta:
        verbose_name = 'песня'
        verbose_name_plural = 'песни'

    def __str__(self) -> str:
        return str(self.title)


class Performer(models.Model):
    """Исполнитель."""
    name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )

    class Meta:
        verbose_name = 'исполнитель'
        verbose_name_plural = 'исполнители'

    def __str__(self) -> str:
        return str(self.name)


class Album(models.Model):
    """Альбом."""
    release_year = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        validators=[validate_past_year]
    )

    performer = models.ForeignKey(
        verbose_name='Исполнитель',
        to='Performer',
        on_delete=models.CASCADE,
        related_name='albums',
    )

    tracks = models.ManyToManyField(
        verbose_name='Песни',
        to='Track',
        through='AlbumTrack',
        related_name='albums',
        blank=True,
    )

    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'

    def __str__(self) -> str:
        return f'{self.pk} от {self.release_year}'


class AlbumTrack(models.Model):
    """Связующая модель между Album и Track."""
    album = models.ForeignKey(
        verbose_name='Альбом',
        to='Album',
        on_delete=models.CASCADE,
        related_name='album_tracks'
    )

    track = models.ForeignKey(
        verbose_name='Песня',
        to='Track',
        on_delete=models.CASCADE,
        related_name='album_tracks'
    )

    track_position = models.PositiveIntegerField(
        verbose_name='Порядковый номер песни в альбоме',
    )

    class Meta:
        unique_together = [
            ['album', 'track'],
            ['album', 'track_position'],
        ]
