from rest_framework import serializers
from .models import *


class LetterSerializer(serializers.ModelSerializer):
    # поле user скрытое и автоматически заполняется данными текущего пользователя
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Letter
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Author
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Room
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = "__all__"

