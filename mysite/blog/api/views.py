from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from blog.models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def viewPosts(request):
    """
    Retrieve all posts.
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewPostDetail(request, pk):
    """
    Retrieve a single post by its ID.
    """
    post = get_object_or_404(Post, id=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)


@api_view(['POST'])
def addPost(request):
    """
    Create a new post.
    """
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def updatePost(request, pk):
    """
    Update an existing post. Supports PUT (full update) and PATCH (partial update).
    """
    post = get_object_or_404(Post, id=pk)
    serializer = PostSerializer(post, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deletePost(request, pk):
    """
    Delete a post by its ID.
    """
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return Response({"message": "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
