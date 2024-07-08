from rest_framework import serializers
from .models import Board
from .models import Comment

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['user', 'nickname', 'title', 'body', 'created_at']
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'nickname', 'comment','created_at']