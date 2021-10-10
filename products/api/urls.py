from django.conf.urls import url, include
from rest_framework import routers
from products.api.views import (
    CategoryView,
    ProductView
)

""" Main router """
router = routers.SimpleRouter()
router.register("categories", CategoryView, basename="categories")
router.register("products", ProductView, basename="products")

urlpatterns = [
    url(r"", include(router.urls)),
]
