from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AccountSerializer
from .models import User
# Create your views here.

class AccountListApiView(APIView):
    def get(self,request):
        Posts = User.objects.all()
        serializer = AccountSerializer(Posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
