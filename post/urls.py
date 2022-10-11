from django.urls import path
from .views import (PostDetail,PostList)
urlpatterns = [
    path('', PostList.as_view(),name='post_list'),
    path('posts/<slug:slug>',PostDetail.as_view(),name='post_detail'),
    path('v1/api/post', PostList.as_view()),
    path('v1/api/post/<int:pk>', PostDetail.as_view()),
    
]