from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (PostDetail,PostList)
urlpatterns = [
    path('', PostList.as_view()),
    path('api/post', PostList.as_view()),
    path('api/post/<int:pk>', PostDetail.as_view()),
    
]