from rest_framework import serializers
from boutique.models.produit import Produit


class ProduitSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Produit
        fields = "__all__"