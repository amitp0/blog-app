from django.urls import path

from .views import CommentDetail, CommentList

urlpatterns = [
    path('api/v1/comment/<int:pk>', CommentDetail.as_view()),
    path('api/v1/comment', CommentList.as_view()),
]
