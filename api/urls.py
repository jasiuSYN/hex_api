from django.urls import path

from . import views

urlpatterns = [
    path("", views.apiOverview, name="apiOverview"),
    path("users/", views.UserListCreate.as_view(), name="users"),
    path("users/<int:pk>", views.ImageUserList.as_view(), name="image_detail"),
    path("image/", views.ImageListCreate.as_view(), name="image"),
    path("tier/", views.TierListCreate.as_view(), name="tier"),
]
