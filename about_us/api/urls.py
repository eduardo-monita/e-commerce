from django.conf.urls import url, include
from rest_framework import routers
from about_us.api.views import CompanyView, ContactView


""" Main router """
router = routers.SimpleRouter()
router.register('company', CompanyView, basename='company')
router.register('contact', ContactView, basename='contact')

urlpatterns = [
    url(r'^', include(router.urls)),
]
