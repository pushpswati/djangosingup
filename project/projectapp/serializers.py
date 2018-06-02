from rest_framework import serializers
from projectapp.models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('created','name','mail','contact','address')

