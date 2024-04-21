from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostsSerializer

class PostsApiView(APIView):
  def get(self, request):
      w = Post.objects.all().values()
      return Response({'data': PostsSerializer(w, many=True).data})

  def post(self, request):
      serializer = PostsSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()

      return Response({"message": serializer.data})

  def put(self, request, *args, **kwargs):
      pk = kwargs.get("pk", None)
      if not pk:
        return Response({"error": "Method PUT not allowed"})

      try:
        instance = Post.objects.get(pk=pk)
      except:
         return Response({"message": "Object does not exists"})

      serializer = PostsSerializer(data=request.data, instance=instance)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({"data": serializer.data})

  def delete(self, request, *args, **kwargs):
      pk = kwargs.get("pk", None)
      if not pk:
        return Response({"error": "Method PUT not allowed"})
      try:
         instance = Post.objects.get(pk=pk)
         instance.delete()
      except:
        return Response({"error": "Object does not exists"})

      return Response({"message": "Success!"})
