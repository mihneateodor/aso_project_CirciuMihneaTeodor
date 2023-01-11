from rest_framework.viewsets import ModelViewSet

from scrumboard.models import List, Card
from scrumboard.serializers import ListSerializer, CardSerializer


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()       # toate obiectele din db
    serializer_class = ListSerializer   # mostenire, functionalitati django rest framework

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer