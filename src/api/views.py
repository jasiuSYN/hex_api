from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Image, User
from .serializers import *

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List or create users": "/users",
        "Images filtered by User": "/users/detail/<int:pk>",
        "List or upload image": "/image",
        "List or create tier": "/tier",
    }
    return Response(api_urls)


# User


class UserListCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# Tier


class TierListCreate(generics.ListCreateAPIView):
    serializer_class = TierSerializer
    queryset = Tier.objects.all()


# Image


class ImageListCreate(generics.ListCreateAPIView):
    serializer_class = ImageListSerializer
    queryset = Image.objects.all()


class ImageUserList(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):

        user = self.kwargs["pk"]
        return Image.objects.filter(user=user)
