from rest_framework import serializers
from boutique.models.categorie import Categorie


class CategorieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Categorie
        fields = "__all__"