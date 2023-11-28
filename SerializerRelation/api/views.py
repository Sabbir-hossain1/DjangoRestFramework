from rest_framework import viewsets
from api.models import Singer, Song
from api.serializers import SongSerializer, SingerSerializer

# Create your views here.
class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    