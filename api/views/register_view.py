from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.user_serializer import UserCreateSerializer


class RegisterView(APIView):

    def post(self, req):
        serializer = UserCreateSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = serializer.save()
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(user.id, status=status.HTTP_201_CREATED)
