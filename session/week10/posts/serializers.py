from rest_framework.serializers import ModelSerializer
from .models import Post, Comment


class PostModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        # fields = '__alll__'
        fields = ['id', 'content']


class PostRetrieveSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        depth = 1


class PostListSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        fields = ['id', 'image', 'content']
        depth = 1


class PostCreateSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        fields = ['image', 'content']


class CommentListModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
