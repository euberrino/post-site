from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.get_all_posts,name="all-posts"),
    path("posts/<str:slug>", views.get_post, name="post-slug")
]
