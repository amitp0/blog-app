from django.urls import path

from .views import PostDetail, PostList

urlpatterns = [
    path('api/v1/post', PostList.as_view()),
    path('api/v1/post/<int:pk>', PostDetail.as_view()),
    path('', PostList.as_view(), name='post_list'),
    path('posts/<slug:slug>', PostDetail.as_view(), name='post_detail'),
]
