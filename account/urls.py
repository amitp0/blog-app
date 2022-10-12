from django.urls import path,include
from .views import (AccountDetail,AccountList)
urlpatterns = [
    path('api/v1/user/<int:pk>', AccountDetail.as_view(),name='profile_detail'),
    path('api/v1/user', AccountList.as_view(),name='account_list'),
    path('accounts/', include('django.contrib.auth.urls')),
]