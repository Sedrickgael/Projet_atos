from rest_framework import viewsets

from boutique.models.vendeur import Vendeur
from boutique.serializers.vendeur import VendeurSerializer


class VendeurViewSet(viewsets.ModelViewSet):
    
    queryset = Vendeur.objects.filter(status=True)
    serializer_class = VendeurSerializer