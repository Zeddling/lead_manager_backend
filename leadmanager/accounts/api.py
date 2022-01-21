from .serializers import UserSerializer, RegisterSerializer
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token

from rest_framework.response import Response


class Logout(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()

        return Response("Logout successful")


class Registration(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = Token.objects.create(user=user)
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": token.key,
            }
        )


class User(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
