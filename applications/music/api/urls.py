from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import AlbumViewSet, PerformerViewSet, TrackViewSet

router_v1 = SimpleRouter()
router_v1.register('albums', AlbumViewSet, basename='albums')
router_v1.register('performers', PerformerViewSet, basename='performers')
router_v1.register('tracks', TrackViewSet, basename='tracks')

urlpatterns = [
    path('', include(router_v1.urls)),
]