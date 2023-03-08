"""messengerdrf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from messenger.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/letterlist/', LetterAPIView.as_view()),
    # path('api/v1/letterdetail/<int:pk>/', LetterAPIView.as_view()),
    path('api/v1/authorlist/', AuthorAPIView.as_view()),
    path('api/v1/authordetail/<int:pk>/', AuthorDetailAPIView.as_view()),
    path('api/v1/roomlist/', RoomAPIView.as_view()),
    path('api/v1/roomdetail/<int:pk>/', RoomDetailAPIView.as_view()),
    path('api/v1/messagelist/', MessageAPIView.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
