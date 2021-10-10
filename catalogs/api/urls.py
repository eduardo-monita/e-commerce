from django.conf.urls import url, include
from rest_framework import routers
from catalogs.api.views import CatalogView

""" Main router """
router = routers.SimpleRouter()
router.register("catalogs", CatalogView, basename="catalogs")

urlpatterns = [
    url(r"", include(router.urls)),
]
