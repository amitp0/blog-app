from django.urls import path, include

urlpatterns = [
    path('post/', include('post.urls')),
    path('comment/', include('comment.urls')),
    path('user/', include('account.urls')),
]
