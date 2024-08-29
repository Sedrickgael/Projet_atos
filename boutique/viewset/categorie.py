from rest_framework import viewsets

from boutique.models.categorie import Categorie
from boutique.serializers.categorie import CategorieSerializer


class CategorieViewSet(viewsets.ModelViewSet):
    
    queryset = Categorie.objects.filter(status=True)
    serializer_class = CategorieSerializer