from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["title", "count"]

    def get_count(self, obj):
        return Post.objects.all().count()
