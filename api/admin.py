from django.contrib import admin
from .models import User, Tier, Image

# Register your models here.
admin.site.register(Tier)
admin.site.register(User)
admin.site.register(Image)
