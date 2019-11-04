from rest_framework import viewsets, permissions

from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_publish=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(
            is_publish=True,
            user=self.request.user,
        )


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
