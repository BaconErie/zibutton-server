from rest_framework import serializers
from api.models import List, Progress

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ['url', 'id', 'name', 'language', 'created', 'updated', 'is_public', 'characters']

class ProgressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Progress
        fields = ['url', 'id', 'user', 'list', 'updated', 'progress']