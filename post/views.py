from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from django.http import Http404
from .models import Post
from comment.models import Comment
from comment.serializers import CommentSerializer
from .serializers import PostSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

class PostList(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    renderer_classes = [TemplateHTMLRenderer,JSONRenderer]
    template_name = 'post/post_list.html'
    def get(self,request):
        Posts=Post.objects.order_by('-created_date')
        serializer=PostSerializer(Posts,many=True)
        # return Response(serializer.data,status.HTTP_200_OK)
        return Response({'posts':serializer.data})
        
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        
class PostDetail(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer,JSONRenderer]
    template_name = 'post/post_detail.html'
    def get_object(self, slug):
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404

    def get(self,request, slug):
        post = self.get_object(slug)
        comment =  Comment.objects.filter(post=post)
        serializer_post = PostSerializer(post)
        serializer_comment = CommentSerializer(comment)
        return Response({'posts':serializer_post.data,'comments':comment})
  
    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self,request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)