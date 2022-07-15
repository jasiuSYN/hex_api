from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class Tier(models.Model):
    tier_name = models.CharField(max_length=200, unique=True, verbose_name="Tier name")
    original_link = models.BooleanField(
        default=False,
        verbose_name="Original image",
        help_text="User can generate originally uploaded image",
    )
    thumbnail_sizes = models.CharField(
        max_length=200,
        verbose_name="Sizes of thubnails",
        help_text="Format: number, number | e.g. 200, 400",
    )
    expiring_link = models.BooleanField(
        default=False,
        verbose_name="Expiring links",
        help_text="User can generate expiring links",
    )

    def __str__(self):
        return self.tier_name


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    password = None
    last_login = None
    tier = models.ForeignKey(
        Tier,
        on_delete=models.CASCADE,
    )
    USERNAME_FIELD = "username"
    objects = UserManager()

    def __str__(self):
        return f"{self.username} {self.tier}"


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    # Validator for image extansion
    image = models.ImageField(
        blank=True, upload_to="", validators=[FileExtensionValidator(["jpeg", "png"])]
    )
