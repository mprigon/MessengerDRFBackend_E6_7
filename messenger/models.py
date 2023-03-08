from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    # blank=True - поле не обязательно к заполнению
    avatar = models.ImageField(upload_to='avatars/', height_field=50, width_field=50, blank=True)

    def __str__(self):
        return self.authorUser.username


class Letter(models.Model):
    sender = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='+')
    recipient = models.ForeignKey('Author', on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'Letter from {self.sender.name} for {self.recipient.name} : {self.text[:128]}'


class Room(models.Model):
    roomName = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.roomName


class Message(models.Model):
    text = models.TextField(max_length=255)
    dateCreation = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'Message in Room {self.room} from {self.author} : {self.text[:128]}'
