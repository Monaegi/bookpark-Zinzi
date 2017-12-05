from django.contrib.auth import get_user_model
from rest_framework import generics, status, mixins
from rest_framework.authtoken.models import Token
from rest_framework.compat import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import SignupSerializer, UserSerializer

User = get_user_model()


class Signup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class Signin(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']

        user = authenticate(
            email=email,
            password=password,
        )

        if user:
            token, token_created = Token.objects.get_or_create(user=user)
            data = {
                'user': UserSerializer(user).data,
                'token': token.key,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                'email': email,
                'password': password,
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)


class Profile(mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)