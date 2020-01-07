from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.api.helpers.is_authenticated import is_authenticated
from recipes.api.serializers.login_serializer import LoginSerializer


class LoginView(APIView):
    def post(self, req):
        serializer = LoginSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if is_authenticated(username=req.data['username'], password=req.data['password']):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
