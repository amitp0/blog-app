from django.urls import path

from .views import CommentDetail, CommentList

urlpatterns = [
    path('v1/api/comment/<int:pk>', CommentDetail.as_view()),
    path('v1/api/comment', CommentList.as_view()),
    path('posts/add_comment', CommentList.as_view(),name='add-comment'),
]
