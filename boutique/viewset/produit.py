from rest_framework import viewsets

from boutique.models.produit import Produit
from boutique.serializers.produit import ProduitSerializer


class ProduitViewSet(viewsets.ModelViewSet):
    
    queryset = Produit.objects.filter(status=True)
    serializer_class = ProduitSerializer