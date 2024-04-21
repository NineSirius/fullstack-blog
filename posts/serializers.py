from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Post


class PostsSerializer(serializers.Serializer):
  content = serializers.CharField()
  created_at = serializers.DateTimeField(read_only=True)
  updated_at = serializers.DateTimeField(read_only=True)
  is_published = serializers.BooleanField(default=True)

  def create(self, validated_data):
    return Post.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.content = validated_data.get("content", instance.content)
    instance.created_at = validated_data.get("created_at", instance.created_at)
    instance.updated_at = validated_data.get("updated_at", instance.updated_at)
    instance.is_published = validated_data.get("is_published", instance.is_published)
    instance.save()
    return instance



  # class Meta:
    # model = Post
    # fields = ("content", "id")
