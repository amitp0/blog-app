from django.urls import path, include

from .views import (AccountDetail, AccountList)

urlpatterns = [
    path('', AccountList.as_view(), name='account_list'),
    path('<int:pk>', AccountDetail.as_view(), name='account_detail'),
]
