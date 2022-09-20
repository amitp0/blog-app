from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PostListApiView,
)
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('authors/',views.author_list,name='author_list'),
    path('api', PostListApiView.as_view()),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


