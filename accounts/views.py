

# Rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView


# Models
from .models import User


# Serailizers
from .serializers import AuthSerailizer


class AuthManager(APIView):

    def post(self, request) -> (Response):
        serializer = AuthSerailizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        atuData = serializer.auth(
            nickName=serializer.data['nickName'],
            password=serializer.data['password'],
            model=User
        )
        return Response(atuData)


class RegisterManager(APIView):

	def post(self,request,mode=None) -> (Response):
		mode = mode
		return Response('REGISTER !!!')




