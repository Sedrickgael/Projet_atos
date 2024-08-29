from rest_framework import viewsets

from boutique.models.tag import Tag
from boutique.serializers.tag import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    
    queryset = Tag.objects.filter(status=True)
    serializer_class = TagSerializer