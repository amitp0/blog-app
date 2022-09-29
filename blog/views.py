from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,Comment,Author
from .forms import PostForm,CommentForm
from django.shortcuts import redirect
# Create your views here.
def author_list(request):
    authors=Author.objects.all()
    return render(request,'blog/author_list.html',{'authors':authors})

def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts':posts,'author':authors})

def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            ath = Author.objects.get(user=request.user)
            post.author = ath
            post.published_date = timezone.now()
            post.save()
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = post.author
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostListApiView(APIView):

    def get(self, request):
        Posts = Author.objects.filter(user = request.user.id)
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'user': request.user.id,
            'first_name': request.data.get('first_name'), 
            'last_name': request.data.get('last_name'),
            'email':request.data.get('email'),
            'registered_at':request.data.get('registered_at'),
            'last_login':request.data.get('last_login'),
            'profile':request.data.get('profile'),
            'profile_photo':request.data.get('profile_photo')
            
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)