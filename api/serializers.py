from django.core.files.images import get_image_dimensions
from easy_thumbnails.files import get_thumbnailer
from rest_framework import serializers

from .models import Image, Tier, User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # To specify the model to be used to create form
        model = User
        # It includes all the fields of model
        fields = "__all__"


# Tier Serializer
class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = "__all__"


# Image Serializer
class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):

    thumbnail_list = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    expiring_link = serializers.SerializerMethodField()

    # generate thumbnails
    def get_thumbnail_list(self, obj):

        # get sizes by Tier from db
        sizes = obj.user.tier.thumbnail_sizes.split(",")
        sizes = [int(size.strip()) for size in sizes]

        # get thumbnail for sizes if height of image is greater than size of thumbnail
        # get url for thumbnails
        height, width = get_image_dimensions(obj.image.path)
        thumb_url = [
            get_thumbnailer(obj.image.path).get_thumbnail({"size": (size, 0)}).url
            for size in sizes
            if height > size
        ]

        # return url for resized img
        return [
            self.context["request"].build_absolute_uri(url[46:]) for url in thumb_url
        ]

    # generate original link or file name
    def get_image(self, obj):
        if obj.user.tier.original_link == True:
            return self.context["request"].build_absolute_uri(obj.image.url)
        else:
            return obj.image.name

    # expiring link
    def get_expiring_link(self, obj):
        return obj.user.tier.expiring_link

    class Meta:
        model = Image
        fields = "__all__"
