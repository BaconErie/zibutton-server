from rest_framework import serializers
from .models import List, Progress

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ['url', 'id', 'name', 'owner', 'language', 'created', 'updated', 'is_public', 'characters']
        extra_kwargs = {
            'name': {'required': True},
            'owner': {'read_only': True},
            'language': {'read_only': True, 'required': True},
            'created': {'read_only': True},
        }


class ProgressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Progress
        fields = ['url', 'id', 'user', 'list', 'updated', 'progress']