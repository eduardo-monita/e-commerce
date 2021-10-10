from django.conf.urls import url, include
from rest_framework import routers

""" Main router """
router = routers.SimpleRouter()
# router.register("example-api", ExampleView, base_name="example-api")

urlpatterns = [
    url(r"", include(router.urls)),
]
