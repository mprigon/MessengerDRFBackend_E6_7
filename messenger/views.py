from django.views.generic.list import MultipleObjectMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import *


class LetterAPIView(generics.ListCreateAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    # если хотим, чтобы авторизация была только по токенам
    # authentication_classes = (TokenAuthentication, )

    # только для авторизованных или всем, но для чтения
    permission_classes = (IsAuthenticatedOrReadOnly, )

    # def get_serializer_context(self):
    #     # Добавляем в контекст
    #     request = super().get_serializer_context()
    #     request['sendername'] = self.sender.name
    #     return {
    #         'request': self.request,
    #         'format': self.format_kwarg,
    #         'view': self,
    #     }

class AuthorAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class AuthorDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class RoomAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class RoomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class MessageAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
