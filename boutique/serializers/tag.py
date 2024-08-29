from rest_framework import serializers
from boutique.models.tag import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"