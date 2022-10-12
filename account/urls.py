from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import (AccountDetail,AccountList)
urlpatterns = [
    path('v1/api/user/<int:pk>', AccountDetail.as_view(),name='profile-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('v1/api/user', AccountList.as_view()),
]