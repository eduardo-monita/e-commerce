from django.conf.urls import url, include
from rest_framework import routers
from posts.api.views import AuthorView, PostView

""" Main router """
router = routers.SimpleRouter()
router.register("authors", AuthorView, basename="authors")
router.register("posts", PostView, basename="posts")

urlpatterns = [
    url(r"", include(router.urls)),
]
