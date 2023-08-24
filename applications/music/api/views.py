from rest_framework.viewsets import ModelViewSet

from .serializers import (
    PerformerSerializer,
    TrackSerializer,
    AlbumSerializer,
)
from ..models import Performer, Track, Album


class PerformerViewSet(ModelViewSet):
    """API-представление для модели Performer."""
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer


class TrackViewSet(ModelViewSet):
    """API-представление для модели Track."""
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class AlbumViewSet(ModelViewSet):
    """API-представление для модели Album."""
    queryset = Album.objects.prefetch_related('tracks')
    serializer_class = AlbumSerializer
