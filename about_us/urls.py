from django.conf.urls import url, include

urlpatterns = [
    url(r"^api/", include("about_us.api.urls"))
]
