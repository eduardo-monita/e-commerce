from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('posts.api.urls'))
]
