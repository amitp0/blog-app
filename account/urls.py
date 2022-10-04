from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (AccountDetail,AccountList)
urlpatterns = [
    path('api/user', AccountList.as_view()),
    path('api/user/<int:pk>', AccountDetail.as_view()),
    
]