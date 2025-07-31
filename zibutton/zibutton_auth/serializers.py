from django.contrib.auth.models import User
from rest_framework import serializers
from zibutton.api.models import List

class UserSerializer(serializers.HyperlinkedModelSerializer):
    lists = serializers.HyperlinkedRelatedField(many=True, queryset=List.objects.all(), view_name='list-detail')
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'lists']
        extra_kwargs = {
            'username': {'required': True, 'read_only': True},
        }