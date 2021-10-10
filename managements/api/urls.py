from django.conf.urls import url, include
from rest_framework import routers
from managements.api.views import HomeView

""" Main router """
router = routers.SimpleRouter()
router.register("home", HomeView, basename="home")

urlpatterns = [
    url(r"", include(router.urls)),
]
