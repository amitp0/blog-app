from django.urls import path
from . import views
from .views import (CommentList,CommentDetail)
urlpatterns = [
    path('api/comment', CommentList.as_view()),
    path('api/comment/<int:pk>', CommentDetail.as_view()),
]