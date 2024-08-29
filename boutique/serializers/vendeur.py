from rest_framework import serializers
from boutique.models.vendeur import Vendeur


class VendeurSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Vendeur
        fields = ['nom_boutique', 'name', 'prenoms', 'adresse']