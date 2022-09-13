from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.shortcuts import redirect
# Create your views here.
# def author_list(request):
#     authors=Authors.objects.all()
#     return render(request,'blog/author_list.html',{'authors':authors})
def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
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
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})